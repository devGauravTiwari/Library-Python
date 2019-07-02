from django.contrib import admin
from .models import Book, Category

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'author']
    list_filter = ['published']
    prepopulated_fields = {'slug':('title','author','edition')}
    search_fields = ['title', 'author']

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display =  ['name' ,'parent']

