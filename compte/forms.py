from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignupForm(UserCreationForm):
    email = forms.EmailField(max_length=200)
    GENDER_CHOICES = [
        ('male', 'Homme'),
        ('female', 'Femme'),
    ]
    gender = forms.ChoiceField(choices=GENDER_CHOICES, widget=forms.RadioSelect, required=True)

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password1', 'password2', 'gender')
