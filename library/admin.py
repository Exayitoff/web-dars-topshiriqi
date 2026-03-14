from django.contrib import admin

from .models import Book, ContactMessage, Genre

admin.site.site_header = "Web Lib Boshqaruv Paneli"
admin.site.site_title = "Web Lib Admin"
admin.site.index_title = "Kutubxona boshqaruvi"


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ("title", "slug", "display_order")
    search_fields = ("title", "description")
    ordering = ("display_order", "title")
    list_per_page = 20
    prepopulated_fields = {"slug": ("title",)}
    fieldsets = (
        ("Asosiy ma'lumot", {"fields": ("title", "slug")}),
        ("Tartib va tavsif", {"fields": ("display_order", "description")}),
    )


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "genre", "year", "is_featured")
    list_filter = ("genre", "is_featured", "year")
    list_editable = ("is_featured",)
    search_fields = ("title", "author", "summary")
    list_select_related = ("genre",)
    list_per_page = 24
    prepopulated_fields = {"slug": ("title",)}
    fieldsets = (
        ("Asosiy ma'lumot", {"fields": ("title", "slug", "author", "genre")}),
        ("Kontent", {"fields": ("summary", "description", "image")}),
        ("Nashr tafsilotlari", {"fields": ("pages", "level", "year", "is_featured")}),
    )


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "subject", "created_at")
    search_fields = ("name", "email", "subject")
    list_filter = ("created_at",)
    readonly_fields = ("name", "email", "subject", "message", "created_at")
    list_per_page = 30

    def has_add_permission(self, request):
        return False
