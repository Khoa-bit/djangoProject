from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.db import IntegrityError
from django.core.exceptions import FieldError

from AppTwo.forms import UserSignUpForm
from AppTwo.management.ModelsFactory import UserFactory


# Create your views here.
def index(request):
    return HttpResponse('<em>My Second App</em>')


def user_help(request):
    return render(request, 'AppTwo/help.html', {'page_title': 'Help Page'})


def get_user_sign_up(request):
    if request.method == 'POST':
        form = UserSignUpForm(request.POST)

        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            print(first_name)
            print(last_name)
            print(email)
            UserFactory(first_name=first_name, last_name=last_name, email=email)
            return HttpResponseRedirect('')

    else:
        form = UserSignUpForm()

    return render(request, 'AppTwo/users.html', {'form': form})
