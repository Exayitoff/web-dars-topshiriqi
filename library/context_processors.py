from library.models import Book, ContactMessage, Genre


def admin_dashboard(request):
    if not request.path.startswith('/admin/'):
        return {}

    return {
        'admin_total_books': Book.objects.count(),
        'admin_total_genres': Genre.objects.count(),
        'admin_total_messages': ContactMessage.objects.count(),
        'admin_featured_books': Book.objects.filter(is_featured=True).count(),
        'admin_recent_messages': ContactMessage.objects.all()[:5],
    }
