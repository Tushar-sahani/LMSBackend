from django.urls import path
from . import views
urlpatterns = [
    path('api/books/', views.listbooks),
    path('api/books/add/', views.addbook),
    path('api/books/<str:isbn>/', views.bookdetails),
    path('api/books/update/<str:isbn>/', views.updatebook),
    path('api/books/delete/<str:isbn>/', views.deletebook),
]
