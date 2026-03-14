const menuToggle = document.querySelector('.menu-toggle');
const nav = document.querySelector('[data-nav]');
const pageKey = document.body.dataset.page;

if (menuToggle && nav) {
  menuToggle.addEventListener('click', () => {
    const isOpen = nav.classList.toggle('is-open');
    menuToggle.setAttribute('aria-expanded', String(isOpen));
  });
}

const navLinks = document.querySelectorAll('[data-nav-link]');

navLinks.forEach((link) => {
  if (link.dataset.navKey === pageKey) {
    link.classList.add('is-current');
  }

  link.addEventListener('click', () => {
    if (nav) {
      nav.classList.remove('is-open');
    }

    if (menuToggle) {
      menuToggle.setAttribute('aria-expanded', 'false');
    }
  });
});

const searchInput = document.querySelector('[data-book-search]');
const filterGroup = document.querySelector('[data-filter-group]');
const bookCards = document.querySelectorAll('[data-book-card]');
const emptyState = document.querySelector('[data-empty-state]');

let activeFilter = 'all';
const params = new URLSearchParams(window.location.search);

const normalize = (value) =>
  value
    .toLowerCase()
    .replace(/’/g, "'")
    .replace(/‘/g, "'");

const applyBookFilters = () => {
  if (!bookCards.length) {
    return;
  }

  const query = normalize(searchInput?.value || '');
  let visibleCount = 0;

  bookCards.forEach((card) => {
    const title = normalize(card.getAttribute('data-title') || card.querySelector('h3')?.textContent || '');
    const author = normalize(card.getAttribute('data-author') || card.querySelector('.meta')?.textContent || '');
    const category = card.getAttribute('data-category') || '';

    const matchesFilter = activeFilter === 'all' || category === activeFilter;
    const matchesQuery = !query || title.includes(query) || author.includes(query);
    const visible = matchesFilter && matchesQuery;

    card.hidden = !visible;

    if (visible) {
      visibleCount += 1;
    }
  });

  if (emptyState) {
    emptyState.hidden = visibleCount !== 0;
  }
};

if (searchInput) {
  const queryParam = params.get('q');

  if (queryParam) {
    searchInput.value = queryParam;
  }

  searchInput.addEventListener('input', applyBookFilters);
}

if (filterGroup) {
  const genreParam = params.get('genre');

  if (genreParam) {
    activeFilter = genreParam;

    filterGroup.querySelectorAll('.filter-chip').forEach((chip) => {
      chip.classList.toggle('is-active', chip.dataset.filter === genreParam);
    });
  }

  filterGroup.addEventListener('click', (event) => {
    const target = event.target;

    if (!(target instanceof HTMLButtonElement)) {
      return;
    }

    activeFilter = target.dataset.filter || 'all';

    filterGroup.querySelectorAll('.filter-chip').forEach((chip) => {
      chip.classList.toggle('is-active', chip === target);
    });

    applyBookFilters();
  });
}

applyBookFilters();
