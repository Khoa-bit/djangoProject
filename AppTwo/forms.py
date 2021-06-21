from django import forms
from django.core.validators import MaxLengthValidator

from AppTwo.models import User


class UserSignUpForm(forms.Form):
    first_name = forms.CharField(label='First name', max_length=63)
    last_name = forms.CharField(label='Last name', max_length=63)
    email = forms.EmailField(label='Email')
    bot_catcher = forms.CharField(required=False, widget=forms.HiddenInput,
                                  validators=[MaxLengthValidator(0)])

    def clean_first_name(self):
        """
        Check if first name is already existed
        :return: None
        """
        first_name = self.cleaned_data['first_name']
        try:
            User.objects.get(first_name=first_name)
            raise forms.ValidationError('First name is already existed',
                                        code='invalid')
        except User.DoesNotExist:
            return first_name
