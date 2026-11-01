// Typeset visible review content and newly opened answers without touching ink.
export function installMath(deck, notice) {
  let queue = Promise.resolve();
  let reportedFailure = false;
  const reportFailure = () => {
    if (reportedFailure) return;
    reportedFailure = true;
    notice('Math formatting could not load. Refresh the page to try again.');
  };

  function typeset(elements) {
    if (!elements.length) return;
    queue = queue.then(async () => {
      if (!await window.tutorialMathReady) { reportFailure(); return; }
      // Answers stay collapsed; their equations are processed when opened.
      document.querySelectorAll('.review-answer').forEach(answer => {
        answer.classList.toggle('mathjax-ignore', !answer.open);
      });
      await window.MathJax.typesetPromise(elements);
      if (deck.isReady()) deck.layout();
      document.dispatchEvent(new CustomEvent('tutorial:layout'));
    }).catch(reportFailure);
  }

  function typesetCurrent() {
    const content = deck.getCurrentSlide()?.querySelector('.review-columns');
    typeset(content ? [content] : []);
  }
  deck.on('ready', typesetCurrent);
  deck.on('slidechanged', typesetCurrent);
  deck.on('overviewshown', () => typeset([...document.querySelectorAll('.review-columns')]));
  document.addEventListener('toggle', event => {
    if (event.target.matches?.('.review-answer') && event.target.open) typeset([event.target]);
  }, true);
}
