// ┬  ┬┌─┐┌┬┐┌─┐
// │  │└─┐ │ └─┐
// ┴─┘┴└─┘ ┴ └─┘
// Functions for printing both lists

const generateLists = () => {
    for (const list of CONFIG.listsContainer) {
        let item = `
        <div class="card list list__${list.id}" id="list_${list.id}">
          <i class="listIcon" icon-name="${list.icon}"></i>
          <a
          target="${CONFIG.openInNewTab ? '_blank' : ''}"
          href="${list.links[0].link}"
          class="listItem"
          >${list.links[0].name}</a>
          <a
          target="${CONFIG.openInNewTab ? '_blank' : ''}"
          href="${list.links[1].link}"
          class="listItem"
          >${list.links[1].name}</a>
          <a
          target="${CONFIG.openInNewTab ? '_blank' : ''}"
          href="${list.links[2].link}"
          class="listItem"
          >${list.links[2].name}</a>
          <a
          target="${CONFIG.openInNewTab ? '_blank' : ''}"
          href="${list.links[3].link}"
          class="listItem"
          >${list.links[3].name}</a>
        </div>
      `;
        const position = 'beforeend';
        lists.insertAdjacentHTML(position, item);
    }
};

generateLists();
