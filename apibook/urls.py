from django.urls import path
app_label='api'
from .views import *
urlpatterns=[
    path('books',BookApiViewAll.as_view(),name='book-list'),
    path('books/<slug:slug>',BookApiView.as_view(),name='book-detail'),
    path('categories',CategoryApiViewAll.as_view(),name='category-list'),
    path('categories/<slug:slug>',CategoryApiView.as_view(),name='category-detail'),
]
