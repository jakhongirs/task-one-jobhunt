from django.shortcuts import render
from rest_framework import generics
from helpers.pagination import CustomPagination
from .serializer import VacancySerializer
from .models import Vacancy, Company, Workers, Category
from rest_framework.views import APIView
from rest_framework.response import Response
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page


# Create your views here.

# ALL VACANCIES:
class AllVacanciesView(APIView):
    serializer_class = VacancySerializer
    queryset = Vacancy.objects.all()
    pagination_class = CustomPagination

    @method_decorator(cache_page(60 * 60 * 2))
    def get(self, *args, **kwargs):
        return super().get(*args, **kwargs)

    def get(self, request, format=None):
        company_count = Company.objects.select_related("company").count()
        vacancy_count = Category.objects.select_related("category").count()
        worker_count = Workers.objects.select_related("workers").count()
        return Response({'company_count': company_count,
                         'vacancy_count': vacancy_count,
                         'workers_count': worker_count})
