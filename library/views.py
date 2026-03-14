from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render

from .forms import ContactMessageForm
from .models import Book, Genre


NAV_ITEMS = [
    {'name': 'Bosh sahifa', 'url_name': 'home', 'key': 'home'},
    {'name': 'Kitoblar', 'url_name': 'books', 'key': 'books'},
    {'name': 'Janrlar', 'url_name': 'genres', 'key': 'genres'},
    {'name': 'Aloqa', 'url_name': 'contact', 'key': 'contact'},
]


def base_context(page_key):
    return {
        'nav_items': NAV_ITEMS,
        'page_key': page_key,
    }


def home(request):
    featured_books = list(Book.objects.select_related('genre').filter(is_featured=True)[:3])
    context = base_context('home')
    context['featured_books'] = featured_books
    context['primary_featured_book'] = featured_books[0] if featured_books else None
    context['secondary_featured_book'] = featured_books[1] if len(featured_books) > 1 else context['primary_featured_book']
    return render(request, 'library/index.html', context)


def books(request):
    context = base_context('books')
    context['books'] = Book.objects.select_related('genre').all()
    context['active_genre'] = request.GET.get('genre', 'all')
    context['search_query'] = request.GET.get('q', '')
    return render(request, 'library/books.html', context)


def genres(request):
    context = base_context('genres')
    context['genres'] = Genre.objects.all()
    return render(request, 'library/genres.html', context)


def book_detail(request, slug):
    context = base_context('books')
    context['book'] = get_object_or_404(Book.objects.select_related('genre'), slug=slug)
    return render(request, 'library/book_detail.html', context)


def contact(request):
    if request.method == 'POST':
        form = ContactMessageForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Xabaringiz muvaffaqiyatli yuborildi. Tez orada siz bilan bog‘lanamiz.')
            return redirect('contact')
    else:
        form = ContactMessageForm()

    context = base_context('contact')
    context['form'] = form
    return render(request, 'library/contact.html', context)
