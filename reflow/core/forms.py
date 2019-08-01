from django import forms
from .models import Candidate


class CandidateForm(forms.ModelForm):
    class Meta:
        model = Candidate
        fields = ('name', 'email', 'skills', 'phone_number', 'github', 'portifolio', 'experiencia', 'sobre',)
        widgets = {
            'name': forms.TextInput(attrs={"class": "form-control"}),
            'email': forms.EmailInput(attrs={"class": "form-control"}),
            'skills': forms.TextInput(attrs={"class": "form-control"}),
            'phone_number': forms.TextInput(attrs={"class": "form-control"}),
            'github': forms.URLInput(attrs={"class": "form-control"}),
            'portifolio': forms.URLInput(attrs={"class": "form-control"}),
            'experiencia': forms.TextInput(attrs={"class": "form-control"}),
            'sobre': forms.TextInput(attrs={"class": "form-control"}),
        }


class EditForm(forms.Form):
    name = forms.CharField(max_length=200)
    skills = forms.CharField(max_length=200)
    phone_number = forms.CharField(max_length=20)
    github = forms.URLField()
    portifolio = forms.URLField(required=False)
    experiencia = forms.CharField(max_length=500, required=False)
    sobre = forms.TextInput()

    widgets = {
        'name': forms.TextInput(attrs={"class": "form-control"}),
        'skills': forms.TextInput(attrs={"class": "form-control"}),
        'phone_number': forms.TextInput(attrs={"class": "form-control"}),
        'github': forms.URLInput(attrs={"class": "form-control"}),
        'portifolio': forms.URLInput(attrs={"class": "form-control"}),
        'experiencia': forms.TextInput(attrs={"class": "form-control"}),
        'sobre': forms.TextInput(attrs={"class": "form-control"}),
    }


class DeleteForm(forms.Form):
    email = forms.EmailField()
