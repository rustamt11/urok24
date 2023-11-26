from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Vacancy
from .forms import VacancyFilterForm

class VacancyListView(ListView):
    model = Vacancy
    template_name = 'vanacy_app/vacancy_list.html'
    context_object_name = 'vacancies'

    def get_queryset(self):
        form = VacancyFilterForm(self.request.GET)
        queryset = super().get_queryset()

        if form.is_valid():
            company = form.cleaned_data.get('company')
            if company:
                queryset = queryset.filter(company=company)

            language = form.cleaned_data.get('language')
            if language:
                queryset = queryset.filter(languages=language)

            experience_level = form.cleaned_data.get('experience_level')
            if experience_level:
                queryset = queryset.filter(experience_level=experience_level)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = VacancyFilterForm(self.request.GET)
        return context

class VacancyDetailView(DetailView):
    model = Vacancy
    template_name = 'vanacy_app/vacancy_detail.html'
    context_object_name = 'vacancy'
