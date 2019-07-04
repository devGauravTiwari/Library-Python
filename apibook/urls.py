from django.urls import path
app_label='api'
from .views import *
urlpatterns=[
    path('books',BookApiViewAll.as_view(),name='book-list'),
   # path('books/<slug:slug>',BookApiView.as_view(),name='book-detail'),
    path('books/create>',BookCreateApiView.as_view(),name='book-create'),
    path('books/<slug:slug>',BookUpdateApiView.as_view(),name='book-update'),
    path('books/<slug:slug>/delete',BookDestroyApiView.as_view(),name='book-delete'),

    path('categories',CategoryApiViewAll.as_view(),name='category-list'),
    path('categories/<slug:slug>',CategoryApiView.as_view(),name='category-detail'),
    path('categories/create',CategoryCreateApiView.as_view(),name='category-create'),
    path('categories/<slug:slug>',CategoryUpdateApiView.as_view(),name='category-update'),
    path('categories/<slug:slug>/delete',CategoryDestroyApiView.as_view(),name='category-delete'),
]
