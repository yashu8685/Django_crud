from django import forms
from app1.models import Emp

class ef(forms.ModelForm):
    class Meta:
        model = Emp

        fields='__all__'