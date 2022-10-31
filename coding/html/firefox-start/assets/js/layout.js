// ┬  ┌─┐┬ ┬┌─┐┬ ┬┌┬┐
// │  ├─┤└┬┘│ ││ │ │
// ┴─┘┴ ┴ ┴ └─┘└─┘ ┴
// Generate Layout.

const generateLayout = () => {
    let buttonsContainer = `
    <div class="buttonsContainer" id="buttons"></div>
  `;
    let listsContainer = `
    <div class="listsContainer" id="lists"></div>
  `;

    const position = 'beforeend';

    linksBlockLeft.insertAdjacentHTML(position, buttonsContainer);
    linksBlockRight.insertAdjacentHTML(position, listsContainer);
    linksBlock.classList.remove('reduceGap');
    linksBlock.classList.remove('removeGap');
};

generateLayout();
