from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from AppTwo.forms import UserSignUpForm
from AppTwo.models import User


# Create your views here.
def index(request):
    return HttpResponse('<em>My Second App</em>')


def user_help(request):
    return render(request, 'AppTwo/help.html', {'page_title': 'Help Page'})


def get_user_sign_up(request):
    if request.method == 'POST':
        form = UserSignUpForm(request.POST)

        if form.is_valid():
            print(form.cleaned_data['first_name'])
            print(form.cleaned_data['last_name'])
            print(form.cleaned_data['email'])
            return HttpResponseRedirect('')

    else:
        form = UserSignUpForm()

    return render(request, 'AppTwo/users.html', {'form': form})
