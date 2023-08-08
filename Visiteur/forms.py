
from django import forms

class ContactForm(forms.Form):
    nom = forms.CharField(label='Votre nom', max_length=100)
    email = forms.EmailField(label='Votre adresse e-mail', max_length=100)
    message = forms.CharField(label='Votre message', widget=forms.Textarea)
