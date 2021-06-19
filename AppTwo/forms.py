from django import forms


class UserSignUpForm(forms.Form):
    first_name = forms.CharField(label='First name', max_length=63)
    last_name = forms.CharField(label='Last name', max_length=63)
    email = forms.EmailField(label='Email')
    bot_catcher = forms.CharField(required=False, widget=forms.HiddenInput)

    # Add form-control class to input tag for Bootstrap 3
    first_name.widget.attrs.update({'class': 'form-control'})
    last_name.widget.attrs.update({'class': 'form-control'})
    email.widget.attrs.update({'class': 'form-control'})
