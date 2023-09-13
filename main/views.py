from django.shortcuts import render, redirect

def home(request):
    return render(request, "home.html")
 
def about(request):
    return render(request, "about.html")

def contacts(request):
    return render(request, "contacts.html")
 
def reviews(request):
    return render(request, "reviews.html")

def news(request):
    return render(request, "news.html")