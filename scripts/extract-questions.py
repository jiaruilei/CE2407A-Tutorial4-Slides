#!/usr/bin/env python3
"""Rebuild the original PDF question snapshots used in Tutorial 4.

Requires Python with Pillow and Poppler's pdftoppm on PATH. The source PDF
is intentionally not bundled; pass the directory containing tutorial
question set 2 with --source-dir. No content is retyped into the snapshots.

Render: 288 dpi = 4 raster pixels per PDF point.
Display: 2 CSS pixels per PDF point (half the PNG's native dimensions).
Crop coordinates are PDF points measured from the top-left of the page.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import shutil
import subprocess
import tempfile

from PIL import Image


REPO = Path(__file__).resolve().parents[1]
DPI = 288
RASTER_SCALE = DPI / 72
CSS_SCALE = 2

# set, page, crop bbox (left, top, right, bottom), slide position (left, top)
CROPS = [
    {
        "file": "set2-q5.png",
        "set": 2,
        "question": 5,
        "page": 3,
        "slide_id": "question-t2-q5",
        "bbox_pt": [
            92,
            354,
            521,
            599
        ],
        "position_css": [
            98,
            132
        ],
        "alt": "Tutorial Set 2, Question 5. The service stations along a highway are located according to a Poisson process with an average of 1 service station in 10 miles. Because of a gas shortage, there is a probability of 0.2 that a service station would not have gasoline available. Assume that the availabilities of gasoline at different service stations are statistically independent. (a) What is the probability that there is at most 1 service station in the next 15 miles of highway? (b) What is the probability that none of the next 3 stations have gasoline for sale? (c) A driver on this highway notices that the fuel gauge in his car reads empty; from experience he knows that he can go another 15 miles. What is the probability that he will be stranded on the highway without gasoline? Hint: the Taylor series expansion for e to the x may be useful: e^x = [1 + x/1! + x^2/2! + x^3/3! + ...]."
    },
    {
        "file": "set2-q9.png",
        "set": 2,
        "question": 9,
        "page": 5,
        "slide_id": "question-t2-q9",
        "bbox_pt": [
            92,
            356,
            521,
            588
        ],
        "position_css": [
            98,
            132
        ],
        "alt": "Tutorial Set 2, Question 9. A concrete column is subjected to an axial load W that is a log-normal random variable with mean = 3000 kN and C.O.V = 0.2. The mean crushing strength (i.e. resistance) of the concrete, R is 35,000 kN per square metre with C.O.V = 0.2. Assume uniform compressive stress over the cross-sectional area of the column, so that the applied stress is S = W/A, where A = cross-sectional area of the column is a constant. (a) What is the distribution of the applied stress? (b) Determine the probability of crushing of a 0.4 m by 0.4 m column. Assume a convenient probability distribution for R. (c) If a failure (crushing) probability of 10^-3 is permitted, determine the required cross-sectional area of the column."
    }
]


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source-dir", required=True, type=Path,
                        help="Directory containing CE2407A Tutorial Questions Set 2.pdf")
    parser.add_argument("--output-dir", type=Path, default=REPO / "assets" / "questions")
    parser.add_argument("--work-dir", type=Path, default=REPO / "tmp" / "question-extraction")
    args = parser.parse_args()
    pdftoppm = shutil.which("pdftoppm")
    if pdftoppm is None:
        parser.error("Poppler pdftoppm was not found on PATH")

    sources = {number: args.source_dir / f"CE2407A Tutorial Questions Set {number}.pdf"
               for number in (2,)}
    for source in sources.values():
        if not source.is_file():
            parser.error(f"Missing source PDF: {source}")
    args.output_dir.mkdir(parents=True, exist_ok=True)
    work_dir = args.work_dir.resolve()
    work_dir.mkdir(parents=True, exist_ok=True)

    manifest = {
        "render_dpi": DPI,
        "raster_pixels_per_pdf_point": RASTER_SCALE,
        "css_pixels_per_pdf_point": CSS_SCALE,
        "coordinate_system": "PDF points from page top-left",
        "sources": [{"set": number, "filename": source.name,
                     "sha256": hashlib.sha256(source.read_bytes()).hexdigest()}
                    for number, source in sources.items()],
        "snapshots": [],
    }
    with tempfile.TemporaryDirectory(prefix="render-", dir=work_dir) as temp:
        # Validate the directory before TemporaryDirectory recursively cleans it.
        if not Path(temp).resolve().is_relative_to(work_dir):
            raise ValueError("Temporary directory is outside the selected work directory")
        page_images: dict[tuple[int, int], Image.Image] = {}
        for number, page in sorted({(crop["set"], crop["page"]) for crop in CROPS}):
            prefix = Path(temp) / f"set{number}-page{page}"
            subprocess.run([pdftoppm, "-f", str(page), "-singlefile", "-r", str(DPI),
                            "-png", str(sources[number]), str(prefix)], check=True)
            page_images[(number, page)] = Image.open(prefix.with_suffix(".png")).convert("RGB")
        for crop in CROPS:
            left, top, right, bottom = crop["bbox_pt"]
            pixel_bbox = tuple(round(value * RASTER_SCALE) for value in (left, top, right, bottom))
            snapshot = page_images[(crop["set"], crop["page"])].crop(pixel_bbox)
            snapshot.save(args.output_dir / crop["file"], optimize=True, dpi=(DPI, DPI))
            dimensions = [(right - left) * CSS_SCALE, (bottom - top) * CSS_SCALE]
            x, y = crop["position_css"]
            if x + dimensions[0] > 1259 or y + dimensions[1] > 700:
                raise ValueError(f"Snapshot exceeds slide-safe area: {crop['file']}")
            manifest["snapshots"].append({**crop, "dimensions_css": dimensions,
                                           "dimensions_px": list(snapshot.size)})
            print(f"{crop['file']}: {snapshot.width}x{snapshot.height}px -> "
                  f"{dimensions[0]}x{dimensions[1]} CSS px at ({x}, {y})")
        for page_image in page_images.values():
            page_image.close()

    (args.output_dir / "manifest.json").write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
