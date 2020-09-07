from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(max_length=256)
    password = forms.CharField(max_length=256,widget=forms.PasswordInput)


class SignUpForm(forms.Form):
    username = forms.CharField(max_length=256)
    password = forms.CharField(max_length=256,widget=forms.PasswordInput)
    confirm_password = forms.CharField(max_length=256,widget=forms.PasswordInput)
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
