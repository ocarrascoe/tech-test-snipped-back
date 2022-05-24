from django.urls import path

from apps.user import views

urlpatterns = [
    path('all', views.UserListView.as_view()),
]
app_name = 'users'
