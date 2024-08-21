from django.contrib import admin
from .models import Book, Review, Comment, Genre

admin.site.register(Book)
admin.site.register(Review)
admin.site.register(Comment)
admin.site.register(Genre)
