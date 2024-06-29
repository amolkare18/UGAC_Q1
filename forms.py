from django import forms
from .models import BOOKLET
from django.contrib.auth.forms import UserCreationForm


class BookletForm(forms.ModelForm):
    class Meta:
        model = BOOKLET
        fields = ['title', 'pdf']

    def clean_pdf_file(self):
        pdf = self.cleaned_data.get('pdf', False)
        if not pdf:
            raise forms.ValidationError("No file selected!")
        return pdf   

