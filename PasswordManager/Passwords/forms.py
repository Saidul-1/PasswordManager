from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(max_length=200, label='Username', widget=forms.TextInput(attrs={'class':'inputs'}))
    password = forms.CharField(max_length=100, widget=forms.PasswordInput(attrs={'class':'inputs'}), label='Password')