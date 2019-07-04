from rest_framework import serializers
from book.models import Book,Category

class BookSerializer(serializers.HyperlinkedModelSerializer):
    url =serializers.HyperlinkedIdentityField(
        lookup_field='slug',
        view_name='book-detail'
    )
    class Meta:
        model = Book
        fields =('url','title','author','edition','thumbnail','kindle','language','published','category')
        extra_kwargs = {
            'category': {'lookup_field': 'slug'}
        }

class CategorySerializer(serializers.HyperlinkedModelSerializer):
    url =serializers.HyperlinkedIdentityField(
        lookup_field='slug',
        view_name='category-detail'
    )
    snippets =serializers.HyperlinkedRelatedField(
        many=True,
        view_name='book-detail',
        read_only=True
    )
    class Meta:
        model = Category
        fields = ('snippets','url','name','description','parent')
        extra_kwargs = {
            'parent': {'lookup_field': 'slug'}
        }
