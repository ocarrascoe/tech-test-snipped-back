from django.urls import path

from apps.borrow import views

urlpatterns = [
    path('', views.BorrowDetailView.as_view()),
    path('book', views.BorrowBookView.as_view()),
]
app_name = 'borrows'
