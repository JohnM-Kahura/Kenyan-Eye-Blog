from django.contrib.auth.forms import UserCreationForm,AuthenticationForm

from django import forms
from django.contrib.auth import authenticate,login,logout
from .models import CustomUser

class UserLoginForm(forms.Form):
    user_name = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self, *args, **kwargs):
        user_name = self.cleaned_data.get('user_name')
        password = self.cleaned_data.get('password')

        if user_name and password:
            user = authenticate(user_name=user_name, password=password)
            if not user:
                raise forms.ValidationError('This user does not exist')
            if not user.check_password(password):
                raise forms.ValidationError('Incorrect password')
            if not user.is_active:
                raise forms.ValidationError('This user is not active')
        return super(UserLoginForm, self).clean(*args, **kwargs)        



class CreateUserForm(UserCreationForm):
    class Meta:
        model=CustomUser
        fields=['user_name','email','password1','password2']
        

class CustomAuthForm(AuthenticationForm):
    class Meta:
        model=CustomUser
        fields=['user_name','password']    