from django import forms
from django.core.validators import MaxLengthValidator

from AppTwo.models import User


class UserSignUpForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']
        error_messages = {
            'first_name': {
                'unique': 'First name already exists'
            }
        }

    bot_catcher = forms.CharField(required=False, widget=forms.HiddenInput,
                                  validators=[MaxLengthValidator(0)])
