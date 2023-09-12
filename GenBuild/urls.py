from django.urls import path
from main import views

urlpatterns = [
    path('', views.home),
    path('about/', views.about),
    path('reviews/', views.reviews),
    path('news/', views.news)
]