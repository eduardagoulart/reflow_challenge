from django import forms
from .models import Candidate


class CandidateForm(forms.ModelForm):
    class Meta:
        model = Candidate
        fields = ('name', 'email', 'skills', 'phone_number', 'github', 'portifolio', 'experiencia', 'resume',)
        widgets = {
            'name': forms.TextInput(attrs={"class": "form-control"}),
            'email': forms.EmailInput(attrs={"class": "form-control"}),
            'skills': forms.TextInput(attrs={"class": "form-control"}),
            'phone_number': forms.TextInput(attrs={"class": "form-control"}),
            'github': forms.URLInput(attrs={"class": "form-control"}),
            'portifolio': forms.URLInput(attrs={"class": "form-control"}),
            'experiencia': forms.TextInput(attrs={"class": "form-control"}),
            'resume': forms.FileInput(attrs={"class": "form-control"}),
        }


class DeleteForm(forms.Form):
    email = forms.EmailField()
