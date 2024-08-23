from django.shortcuts import render
from rest_framework import viewsets
from .models import Book, Review, Comment
from .serializers import BookSerializer, ReviewSerializer, CommentSerializer
from django.shortcuts import render


def home(request):
    return render(request, 'index.html')


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
