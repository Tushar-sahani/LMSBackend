from django.urls import path
from . import views
urlpatterns = [
    path('api/books/', views.listbooks),
    path('api/books/add/', views.addbook),
    path('api/books/<isbn>/', views.bookdetails),
    path('api/books/update/<isbn>/', views.updatebook),
    path('api/books/delete/<isbn>/', views.deletebook),
]
