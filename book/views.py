from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Book
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import CreateView
from django.contrib.auth.models import User

@login_required
def dashboard(request):
    return render(request,'account/dashboard.html',{'section': 'dashboard'})

class BookListView(ListView):
    model = Book
    template_name = 'book/book_list.html'
    context_object_name = 'books'

class BookDetailView(DetailView):
    model = Book
    template_name = 'book/book_detail.html'
    context_object_name = 'book'

class RegisterUserView(CreateView):
    model = User
    template_name = 'registration/sineup.html'
    fields = ['username','email','password']
    success_url = '/login'
