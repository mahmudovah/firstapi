from django.urls import path
from main import views

urlpatterns = [
    path('', views.first_api, name='firs_tapi'),
    path('books/',views.books_api),
    path('authors/', views.author_api),
    path('categorys/', views.category_api),
    path('books/<int:pk>/', views.book_detail),
    path('me/', views.me_api, name='me_api')
]