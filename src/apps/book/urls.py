from django.urls import path

from apps.book import views

urlpatterns = [
    path('', views.BookDetailView.as_view()),
    path('<int:book_id>', views.BookView.as_view()),
    path('all', views.BookListView.as_view()),
    path('available', views.BookAvailableListView.as_view()),
    path('borrowed', views.BookBorrowedListView.as_view()),
]
app_name = 'books'
