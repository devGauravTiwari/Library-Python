from django.urls import path
from .views import BookListView ,BookDetailView, RegisterUserView

urlpatterns = [
    path('',BookListView.as_view(),name='all_books'),
    path('<slug:slug>',BookListView.as_view(),name='books'),
    path('book/<slug:slug>',BookDetailView.as_view(),name='book'),
    path('signup/',RegisterUserView.as_view() ,name='signup'),
]
