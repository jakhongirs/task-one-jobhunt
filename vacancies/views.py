from django.shortcuts import render
from rest_framework import generics
from helpers.pagination import CustomPagination
from .serializer import VacancySerializer
from .models import Vacancy
from django.db.models import Count
from django.db.models import Q


# Create your views here.

# ALL VACANCIES:
class AllVacanciesView(generics.ListAPIView):
    queryset = Vacancy.objects.all()
    serializer_class = VacancySerializer
    pagination_class = CustomPagination

    def get_queryset(self):
        return self.queryset.annotate(vacancy_count=Count('title')).annotate(
            company_count=Count('company__title')).annotate(
            workers_count=Count('category__workers__name'))
