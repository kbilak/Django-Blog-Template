from django.utils.translation import gettext as _
from .models import Contact
from django import forms


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['email', 'message']