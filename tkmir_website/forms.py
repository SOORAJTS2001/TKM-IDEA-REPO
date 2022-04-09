from .models import Register,Login
from django import forms
class RegisterForm(forms.ModelForm):
    email = forms.EmailField()
    password = forms.PasswordInput()
    class Meta:

        model = Register
        fields = ['first_name','last_name','email','password']
class LoginForm(forms.ModelForm):
    class Meta:
        password = forms.PasswordInput()
        model = Login
        fields = ['email','password']

