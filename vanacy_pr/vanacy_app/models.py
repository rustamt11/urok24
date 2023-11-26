from django.db import models

class Company(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class ProgrammingLanguage(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Vacancy(models.Model):
    title = models.CharField(max_length=200)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    languages = models.ManyToManyField(ProgrammingLanguage)
    EXPERIENCE_LEVELS = (
        ('JR', 'Junior'),
        ('MD', 'Middle'),
        ('SR', 'Senior'),
    )
    experience_level = models.CharField(max_length=2, choices=EXPERIENCE_LEVELS)

    def __str__(self):
        return self.title
