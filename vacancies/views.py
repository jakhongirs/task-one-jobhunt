from django.shortcuts import render
from rest_framework import generics
from helpers.pagination import CustomPagination
from .serializer import VacancySerializer
from .models import Vacancy, Company, Workers, Category
from django.db.models import Count
from django.db.models import Q
from rest_framework.views import APIView
from rest_framework.response import Response


# Create your views here.

# ALL VACANCIES:
class AllVacanciesView(APIView):
    serializer_class = VacancySerializer
    queryset = Vacancy.objects.all()

    def get(self, request, format=None):
        company_count = Company.objects.all().count()
        vacancy_count = Category.objects.all().count()
        worker_count = Workers.objects.all().count()
        return Response({'company_count': company_count,
                         'vacancy_count': vacancy_count,
                         'worker_count': worker_count})
