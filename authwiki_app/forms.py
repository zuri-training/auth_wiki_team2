from django import forms
from authwiki_app.models import Contact

class Contactforms(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'message']
