from django import forms
from django_recaptcha.fields import ReCaptchaField
from django_recaptcha.widgets import ReCaptchaV2Checkbox

class LoginForm(forms.Form):
    username = forms.CharField(max_length=200, label='Username', widget=forms.TextInput(attrs={'class':'inputs'}))
    password = forms.CharField(max_length=100, widget=forms.PasswordInput(attrs={'class':'inputs'}), label='Password')
    captcha = ReCaptchaField(widget=ReCaptchaV2Checkbox)