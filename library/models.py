from django.db import models
from django.urls import reverse


class Genre(models.Model):
    title = models.CharField(max_length=120)
    slug = models.SlugField(unique=True)
    description = models.TextField()
    display_order = models.PositiveSmallIntegerField(default=0)

    class Meta:
        ordering = ['display_order', 'title']

    def __str__(self):
        return self.title


class Book(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    author = models.CharField(max_length=120)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE, related_name='books')
    description = models.TextField()
    summary = models.TextField()
    image = models.URLField()
    pages = models.PositiveIntegerField()
    level = models.CharField(max_length=60)
    year = models.PositiveSmallIntegerField()
    is_featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title

    @property
    def category(self):
        return self.genre.slug

    @property
    def category_label(self):
        return self.genre.title

    def get_absolute_url(self):
        return reverse('book_detail', kwargs={'slug': self.slug})


class ContactMessage(models.Model):
    name = models.CharField(max_length=120)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.name} - {self.subject}'
