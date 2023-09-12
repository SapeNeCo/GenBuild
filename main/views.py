from django.shortcuts import render

def home(request):
    return render(request, "home.html")
 
def about(request):
    return render(request, "about.html")
 
def reviews(request):
    return render(request, "reviews.html")

def news(request):
    return render(request, "news.html")