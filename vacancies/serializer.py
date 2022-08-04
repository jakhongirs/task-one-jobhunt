from rest_framework import serializers
from .models import Vacancy, Category, Company


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = "__all__"


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class VacancySerializer(serializers.ModelSerializer):
    # company = CompanySerializer()
    # category = CategorySerializer()
    company_count = serializers.IntegerField()
    vacancy_count = serializers.IntegerField()
    workers_count = serializers.IntegerField()

    class Meta:
        model = Vacancy
        fields = ('company_count', 'workers_count', 'vacancy_count')
