const contents = document.querySelector('.contents');
const mobile = window.matchMedia('(max-width: 900px)');
if (contents && mobile.matches) contents.open = false;
mobile.addEventListener('change', event => {
  if (contents) contents.open = !event.matches;
});

const search = document.querySelector('#chapter-search');
search?.addEventListener('input', () => {
  const query = search.value.trim().toLocaleLowerCase();
  for (const group of document.querySelectorAll('.nav-group')) {
    let visible = false;
    for (const item of group.querySelectorAll('li')) {
      item.hidden = !item.textContent.toLocaleLowerCase().includes(query);
      visible ||= !item.hidden;
    }
    group.hidden = !visible;
  }
});
