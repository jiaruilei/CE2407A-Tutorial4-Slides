# CE2407A Tutorial 4

Six web slides for Tutorial 4, Week 12, covering Tutorial Questions Set 2, Q5 and Q9.

1. Tutorial 4 cover and QR link
2. Q5: Original question statement and Taylor-series hint
3. Q5: Stations and fuel range interactive exercise
4. Q9: Original question statement and stress equation
5. Q9: Column sizing interactive exercise
6. Blank whiteboard for handwritten equations

## Present

Open [the presentation](https://jiaruilei.github.io/CE2407A-Tutorial4-Slides/). Use the arrow keys or bottom buttons to change slides. Press O for overview and F for full screen. When an exercise has keyboard focus, use the bottom buttons to change slides.

The top menu jumps to **Question**, **Explore**, or **Whiteboard**. **View larger** opens a question snapshot with zoom, pan and Fit width controls. **Open exercise** opens the current question in a separate tab. The cover QR code links to this deck.

**Enlarge exercise** fills the slide, and **Back to slide** restores its layout. **More → Reset exercise** resets only that exercise and its chat. Leaving an exercise slide preserves its calculations and chat. Results and worked solutions start hidden and appear after Calculate.

Both exercises need an internet connection and embed [CE2407A_Tutorial2](https://jiaruilei.github.io/CE2407A_Tutorial2/) with `question=q5` or `question=q9` and `embed=1`. The existing app provides the calculations, plots and optional AI coaching. No API keys belong in this repository.

Full screen uses the browser's standard or WebKit fullscreen API. If native full screen is unavailable, **Expand view** uses the browser window with compact controls. Select **Exit view** to return. Phones keep the same slide layout; landscape orientation or View larger improves readability.

## Annotate

Select **Ink** to open the pen, highlighter, eraser, color and thickness controls. Undo, Redo and Clear ink apply to the current slide view; clearing is undoable. Choose **Pointer** or press Escape to interact with an exercise. Ctrl+Z undoes ink and Ctrl+Y or Ctrl+Shift+Z redoes it while the toolbar is open. Text fields keep their normal editing shortcuts.

Ink is saved automatically in this browser on this device under `ce2407a-tutorial4-slides:ink:v1`, independently of the other tutorial decks. It is not synced to GitHub or other devices. Use one presentation tab when annotating the same slide. If storage is unavailable, ink remains while the tab is open.

Ink over an embedded exercise follows its main page when it scrolls. Scrolling nested panels or changing the exercise content does not reposition existing ink. Normal and enlarged exercises keep separate ink because content reflows. Full screen and window resizing preserve alignment. Ink remains visible when its toolbar is closed.

The final whiteboard uses the same annotation tools and saving behavior. It is available from the question menu or after the Q9 exercise.

## Design and source assets

The layout and controls follow [CE2407A-Tutorial1-Slides](https://github.com/jiaruilei/CE2407A-Tutorial1-Slides): 1280 × 720 slides, Arial, navy `#13294b`, orange `#ed7d31`, the same cover, question and interactive layouts, and the same ink and full-screen behavior. The CSS, question viewer, fullscreen controller and bundled Reveal.js are unchanged from Tutorial 1. Tutorial 2 supplies the existing whiteboard and per-question navigation support.

Question headings stay at x=97.92, y=32 in 52px Arial. Snapshots begin at x=98, y=132 and use 2 CSS pixels per PDF point, rendered at 288 dpi for crisp display. Q5 occupies 858 × 490 CSS pixels; Q9 occupies 858 × 464. Both include the complete question and all parts without retyping the source.

Snapshots come from pages 3 and 5 of the supplied `CE2407A Tutorial Questions Set 2.pdf`. `assets/questions/manifest.json` records the source checksum, page numbers, crop bounds, dimensions, placement and accessible text. The PDF is not included.

To rebuild snapshots, install Pillow and Poppler, then run:

```sh
python scripts/extract-questions.py --source-dir "path/to/source-pdfs"
```

Stable slide IDs are `slide-1`, `question-t2-q5`, `slide-2`, `question-t2-q9`, `slide-3`, and `whiteboard`. Preserve these IDs and the ink namespace when updating this deck. Reveal.js is bundled with its license in `LICENSE-reveal.txt`.

## Preview and checks

Run `python -m http.server 4174` here and open [http://localhost:4174](http://localhost:4174). Local previews use the live exercises; ink following iframe scrolling requires the shared GitHub Pages origin available on the published site. Run `npm test` with Node.js to check annotation storage/history, coordinate handling and fullscreen behavior.

## Publish

GitHub Pages serves the repository root from the `main` branch. No build step is required. Push updates to `main` to publish them.
