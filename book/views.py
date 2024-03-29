from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Book, Category
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import CreateView
from django.contrib.auth.models import User

@login_required
def dashboard(request):
    return render(request,'account/dashboard.html',{'section': 'dashboard'})

class BookListView(ListView):
    model = Book
    template_name = 'book/book_list.html'
    def collect(self,category):
        Queryset=Book.objects.none()
        while(category.has_children()):
            for category in category.children.all() :
                Queryset=Queryset.union(self.collect(category))

        Queryset=Queryset.union(Book.objects.filter(category=category))
        return Queryset
    def get_context_data(self,**kwargs):
        context =super().get_context_data(**kwargs)
        #get only those who has no parent
        context['categorys']=Category.objects.filter(parent=None).all()
        mycontex=Book.objects
        try:
            if(self.kwargs['slug']):
                cat=Category.objects.filter(slug=self.kwargs['slug']).get()
                mycontex=self.collect(category=cat)
        except:
            pass
        context['books']=mycontex.all()
        context['rolls']=[i for i in range(190000000,190149721)]
        return context

class BookDetailView(DetailView):
    model = Book
    template_name = 'book/book_detail.html'
    context_object_name = 'book'

class RegisterUserView(CreateView):
    model = User
    template_name = 'registration/sineup.html'
    fields = ['username','email','password']
    success_url = '/login'
