from django.contrib import admin
from .models import Company, ProgrammingLanguage, Vacancy
# Register your models here.
admin.site.register(Company)
admin.site.register(ProgrammingLanguage)
admin.site.register(Vacancy)