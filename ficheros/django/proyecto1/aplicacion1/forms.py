from django import forms

class Formulario(forms.Form):
    nombre = forms.CharField()
    email = forms.EmailField()