from django import forms

class UserForm(forms.Form):
    userName = forms.CharField(label='UserName', max_length=100)
    password = forms.CharField(label='Password', widget=forms.PasswordInput())