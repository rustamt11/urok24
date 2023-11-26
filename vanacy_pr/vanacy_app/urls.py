from django.urls import path
from .views import VacancyListView, VacancyDetailView

urlpatterns = [
    path('', VacancyListView.as_view(), name='vacancy_list'),
    path('vacancy/<int:pk>/', VacancyDetailView.as_view(), name='vacancy_detail'),
]
