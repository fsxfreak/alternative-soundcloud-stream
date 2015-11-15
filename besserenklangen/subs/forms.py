from django import forms

class UserForm(forms.Form):
    username = forms.CharField(label="Soundcloud username", max_length = 100)