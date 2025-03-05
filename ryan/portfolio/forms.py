from django import forms
from .models import Contact_info

class Contact_form(forms.ModelForm):
    class Meta:
        model = Contact_info
        fields = ['first_name', 'second_name', 'email', 'message']