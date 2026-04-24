from django.urls import path
from .views import *

urlpatterns = [
    path('books/', book_api, name='book_api'),
    path('authors/', author_api, name='author')
]