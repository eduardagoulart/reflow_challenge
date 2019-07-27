from django import forms
from .models import Candidate


class CandidateForm(forms.ModelForm):
    class Meta:
        model = Candidate
        fields = ('name', 'email', 'skills', 'phone_number', 'github', 'portifolio', 'experiencia', 'resume', )