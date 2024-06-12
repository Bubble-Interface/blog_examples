from django.urls import include, path
from books import views as book_views

urlpatterns = [
    path('', book_views.books, name="books")
]
