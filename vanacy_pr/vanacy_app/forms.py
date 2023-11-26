from django import forms
from .models import Company, ProgrammingLanguage, Vacancy


class VacancyFilterForm(forms.Form):
    company = forms.ModelChoiceField(queryset=Company.objects.all(), required=False)
    language = forms.ModelChoiceField(queryset=ProgrammingLanguage.objects.all(), required=False)
    experience_level = forms.ChoiceField(choices=Vacancy.EXPERIENCE_LEVELS, required=False)
