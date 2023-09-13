from django.urls import path
from main import views

urlpatterns = [
    path('', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('contacts/', views.contacts, name="contacts"),
    path('reviews/', views.reviews, name="reviews"),
    path('news/', views.news, name="news")
]