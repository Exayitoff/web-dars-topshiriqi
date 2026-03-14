from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('books/', views.books, name='books'),
    path('books/<slug:slug>/', views.book_detail, name='book_detail'),
    path('genres/', views.genres, name='genres'),
    path('contact/', views.contact, name='contact'),
]
