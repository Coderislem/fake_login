from django import forms
from .models import Profile

class FacebookLoginForm(forms.ModelForm):
    email = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Email or phone number'
            }
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Password'
            }
        )
    )

    class Meta:
        model = Profile
        fields = ['email', 'password']
