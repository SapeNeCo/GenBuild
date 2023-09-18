from django.shortcuts import render
from django_user_agents.utils import get_user_agent

def home(request):
    user = get_user_agent(request)
    if user.is_pc:
        return render(request, "pc/home.html")
    else:
        return render(request, "mobile/home_m.html")
 
def about(request):
    user = get_user_agent(request)
    if user.is_pc:
        return render(request, "pc/about.html")
    else:
        return render(request, "mobile/about_m.html")

def contacts(request):
    user = get_user_agent(request)
    if user.is_pc:
        return render(request, "pc/contacts.html")
    else:
        return render(request, "mobile/contacts_m.html")
 
def reviews(request):
    user = get_user_agent(request)
    if user.is_pc:
        return render(request, "pc/reviews.html")
    else:
        return render(request, "mobile/reviews_m.html")

def news(request):
    user = get_user_agent(request)
    if user.is_pc:
        return render(request, "pc/news.html")
    else:
        return render(request, "mobile/news_m.html")

def partners(request):
    user = get_user_agent(request)
    if user.is_pc:
        return render(request, "pc/partners.html")
    else:
        return render(request, "mobile/partners_m.html")