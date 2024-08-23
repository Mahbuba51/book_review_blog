from django.urls import path, include, re_path
from rest_framework.routers import DefaultRouter
from .views import BookViewSet, ReviewViewSet, CommentViewSet, home

router = DefaultRouter()
router.register(r'books', BookViewSet)
router.register(r'reviews', ReviewViewSet)
router.register(r'comments', CommentViewSet)

urlpatterns = [
    # path('', home, name='home'),
    path('', include(router.urls)),
]
