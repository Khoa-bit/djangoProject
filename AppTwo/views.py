from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(response):
    return HttpResponse('<em>My Second App</em>')


def user_help(response):
    return render(response, 'AppTwo/help.html', {'page_title': 'Help Page'})
