# CE2407A Tutorial 4

Fourteen web slides for Tutorial 4, Week 12: a quiz review of Lectures 1–5, followed by Tutorial Questions Set 2, Q5 and Q9.

1. Tutorial 4 cover and QR link
2. Quiz scope
3. Uncertainty and histograms
4. Events and independence
5. Conditional probability and Bayes
6. Random variables, probabilities and moments
7. Normal distribution
8. Lognormal distribution
9. Q5: Original question statement and Taylor-series hint
10. Q5: Lecture notes on the Poisson process and distribution
11. Q5: Stations and fuel range interactive exercise
12. Q9: Original question statement and stress equation
13. Q9: Lecture notes with the standard normal table
14. Q9: Column sizing interactive exercise

## Quiz review

The seven review slides include quick checks with **Show answer** and room for handwriting. Use **Pointer** when opening an answer, then select the pen to continue writing. Lecture links open the corresponding Canvas notes and require course access. Supporting teaching cues and source details are stored in each slide's HTML notes.

Coverage follows the [28 October announcement](https://canvas.nus.edu.sg/courses/93981/discussion_topics/510267): Lectures 1–5, including normal and lognormal distributions. Lectures 6–7, blended-learning materials and MATLAB are excluded. The given exponential PDF example in Lecture 4 remains part of the covered notes. Q5 and Q9 follow as regular tutorial work involving later topics.

## Present

Open [the presentation](https://jiaruilei.github.io/CE2407A-Tutorial4-Slides/). Use the arrow keys or bottom buttons to change slides. Press O for overview and F for full screen. When an exercise has keyboard focus, use the bottom buttons to change slides.

The top menu jumps to each review topic, **Question**, **Notes**, or **Explore**. **View larger** opens a question snapshot or lecture-notes page with zoom, pan and Fit width controls. It preserves the panel layout and leaves slide ink intact. **Open exercise** opens the current question in a separate tab. The cover QR code links to this deck.

**Enlarge exercise** fills the slide, and **Back to slide** restores its layout. **More → Reset exercise** resets only that exercise and its chat. Leaving an exercise slide preserves its calculations and chat. Results and worked solutions start hidden and appear after Calculate.

Both exercises need an internet connection and embed [CE2407A_Tutorial2](https://jiaruilei.github.io/CE2407A_Tutorial2/) with `question=q5` or `question=q9` and `embed=1`. The existing app provides the calculations, plots and optional AI coaching. No API keys belong in this repository.

Full screen uses the browser's standard or WebKit fullscreen API. If native full screen is unavailable, **Expand view** uses the browser window with compact controls. Select **Exit view** to return. Phones keep the same slide layout; landscape orientation or View larger improves readability.

## Annotate

Select **Ink** to open the pen, highlighter, eraser, color and thickness controls. Undo, Redo and Clear ink apply to the current slide view; clearing is undoable. Choose **Pointer** or press Escape to interact with an exercise. Ctrl+Z undoes ink and Ctrl+Y or Ctrl+Shift+Z redoes it while the toolbar is open. Text fields keep their normal editing shortcuts.

Ink is saved automatically in this browser on this device under `ce2407a-tutorial4-slides:ink:v1`, independently of the other tutorial decks. It is not synced to GitHub or other devices. Use one presentation tab when annotating the same slide. If storage is unavailable, ink remains while the tab is open.

Ink over an embedded exercise follows its main page when it scrolls. Scrolling nested panels or changing the exercise content does not reposition existing ink. Normal and enlarged exercises keep separate ink because content reflows. Full screen and window resizing preserve alignment. Ink remains visible when its toolbar is closed.

## Design and source assets

The layout and controls follow [CE2407A-Tutorial1-Slides](https://github.com/jiaruilei/CE2407A-Tutorial1-Slides): 1280 × 720 slides, Arial, navy `#13294b`, orange `#ed7d31`, the same cover, question and interactive layouts, and the same ink and full-screen behavior. The base CSS changes only the menu layout to accommodate Notes; the fullscreen controller and bundled Reveal.js are unchanged. The question viewer also copies image clipping for the notes panels. Review-specific styling is scoped in `review.css` and uses the same question-heading position and size. The Question / Notes / Explore navigation follows the established tutorial decks.

Question headings stay at x=97.92, y=32 in 52px Arial. Snapshots begin at x=98, y=132 and use 2 CSS pixels per PDF point, rendered at 288 dpi for crisp display. Q5 occupies 858 × 490 CSS pixels; Q9 occupies 858 × 464. Both include the complete question and all parts without retyping the source.

Snapshots come from pages 3 and 5 of the supplied `CE2407A Tutorial Questions Set 2.pdf`. `assets/questions/manifest.json` records the source checksum, page numbers, crop bounds, dimensions, placement and accessible text. The PDF is not included.

Lecture notes use the supplied `Q5.png` and `Q9.png`, copied byte-for-byte into `assets/lecture-notes`. CSS clipping displays their original content in two side-by-side panels beginning at x=98 and x=652, y=132, each 530px wide. Q5 separates the Poisson assumptions from the derivation. Q9 repeats the original table header above the continued rows and omits only the blank left margin. Source annotations remain intact. `assets/lecture-notes/manifest.json` records the checksums, source regions and placement. Each notes page has independent saved ink.

To rebuild snapshots, install Pillow and Poppler, then run:

```sh
python scripts/extract-questions.py --source-dir "path/to/source-pdfs"
```

Stable slide IDs are `slide-1`, `question-t2-q5`, `notes-t2-q5`, `slide-2`, `question-t2-q9`, `notes-t2-q9`, `slide-3`, `review-scope`, `review-uncertainty`, `review-events`, `review-bayes`, `review-random-variables`, `review-normal`, and `review-lognormal`. Preserve these IDs and the ink namespace when updating this deck so existing saved annotations remain attached to the right content. The retired `whiteboard` ink key remains accepted internally so older saved annotations can still be loaded. Reveal.js is bundled with its license in `LICENSE-reveal.txt`.

## Preview and checks

Run `python -m http.server 4174` here and open [http://localhost:4174](http://localhost:4174). Local previews use the live exercises; ink following iframe scrolling requires the shared GitHub Pages origin available on the published site. Run `npm test` with Node.js to check annotation storage/history, coordinate handling and fullscreen behavior.

## Publish

GitHub Pages serves the repository root from the `main` branch. No build step is required. Push updates to `main` to publish them.
