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
    company = CompanySerializer()
    category = CategorySerializer()

    class Meta:
        model = Vacancy
        fields = "__all__"
