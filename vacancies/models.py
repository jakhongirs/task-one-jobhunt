from django.db import models
from helpers.models import BaseModel


# Create your models here.

# CATEGORY:
class Category(BaseModel):
    title = models.CharField(max_length=128)
    slug = models.CharField(max_length=128, unique=True)

    def __str__(self):
        return self.title


# COMPANY:
class Company(BaseModel):
    title = models.CharField(max_length=128)
    slug = models.CharField(max_length=128, unique=True)

    def __str__(self):
        return self.title


# VACANCY:
class Vacancy(BaseModel):
    title = models.CharField(max_length=128)
    slug = models.CharField(max_length=128, unique=True)
    content = models.TextField()
    published_datetime = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    company_name = models.CharField(max_length=128)
    min_salary = models.IntegerField(default=0, null=True, blank=True)
    max_salary = models.IntegerField(default=0, null=True, blank=True)
    is_interview_salary = models.BooleanField(default=False)

    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='vacancies')

    def __str__(self):
        return self.title


# WORKERS:
class Workers(BaseModel):
    name = models.CharField(max_length=128)
    address = models.CharField(max_length=128)

    def __str__(self):
        return self.name
