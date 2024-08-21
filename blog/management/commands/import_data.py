import csv
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from blog.models import Book, Genre, Review


class Command(BaseCommand):
    help = 'Import data from CSV files'

    def handle(self, *args, **kwargs):
        self.import_genres()
        self.import_books()
        self.import_users()
        self.import_reviews()
        self.stdout.write(self.style.SUCCESS('Data imported successfully'))

    def import_genres(self):
        with open('blog/data/genres.csv', 'r') as file:
            reader = csv.DictReader(file)
            genres = [Genre(name=row['name']) for row in reader]
            Genre.objects.bulk_create(genres)
        self.stdout.write(self.style.SUCCESS('Genres imported successfully'))

    def import_books(self):
        with open('blog/data/books.csv', 'r') as file:
            reader = csv.DictReader(file)
            books = []
            for row in reader:
                book = Book(
                    title=row['title'],
                    author=row['author'],
                    publication_date=row['publication_date']
                )
                books.append(book)
            Book.objects.bulk_create(books)
            self.assign_genres_to_books()
        self.stdout.write(self.style.SUCCESS('Books imported successfully'))

    def import_users(self):
        usernames = ['reviewer']  # Add other usernames if needed
        for username in usernames:
            if not User.objects.filter(username=username).exists():
                User.objects.create_user(username=username, password='password123')
        self.stdout.write(self.style.SUCCESS('Users imported successfully'))

    def import_reviews(self):
        with open('blog/data/reviews.csv', 'r') as file:
            reader = csv.DictReader(file)
            reviews = []
            for row in reader:
                book = Book.objects.get(title=row['book_title'])
                user, created = User.objects.get_or_create(username=row['author_username'],
                                                           defaults={'password': 'password123'})
                review = Review(
                    book=book,
                    author=user,
                    content=row['content'],
                    rating=row['rating']
                )
                reviews.append(review)
            Review.objects.bulk_create(reviews)
        self.stdout.write(self.style.SUCCESS('Reviews imported successfully'))

    def assign_genres_to_books(self):
        genres = Genre.objects.all()
        for book in Book.objects.all():
            if 'Fantasy' in book.title:
                book.genres.add(*genres.filter(name='Fantasy'))
            elif 'Sci-Fi' in book.title:
                book.genres.add(*genres.filter(name='Sci-Fi'))
            book.save()
