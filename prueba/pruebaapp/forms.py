from django import forms
from pruebaapp.models import integrante






class Formproyecto(forms.ModelForm):
    class Meta:
        model = integrante
        fields = '__all__'