'use strict';

// Match the exercises' locally bundled renderer; no CDN or font download needed.
let resolveMathReady;
window.tutorialMathReady = new Promise(resolve => { resolveMathReady = resolve; });
window.MathJax = {
  tex: {
    inlineMath: [['\\(', '\\)']],
    displayMath: [['\\[', '\\]']],
    processEscapes: true,
    packages: ['base', 'ams', 'newcommand', 'configmacros']
  },
  svg: { fontCache: 'local', scale: 1, displayAlign: 'left' },
  options: {
    ignoreHtmlClass: 'notes|mathjax-ignore',
    enableMenu: false,
    enableAssistiveMml: true,
    menuOptions: { settings: { assistiveMml: true, collapsible: false, explorer: false } },
    renderActions: { addMenu: [], checkLoading: [] }
  },
  loader: { failed: () => resolveMathReady(false) },
  startup: {
    typeset: false,
    ready() {
      try {
        MathJax.startup.defaultReady();
        MathJax.startup.promise.then(() => resolveMathReady(true), () => resolveMathReady(false));
      } catch (_) { resolveMathReady(false); }
    }
  }
};
document.addEventListener('error', event => {
  if (event.target?.id === 'MathJax-script') resolveMathReady(false);
}, true);
