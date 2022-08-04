from django.contrib import admin
from vacancies.models import Vacancy, Category, Company, Workers

# Register your models here.
admin.site.register(Vacancy)
admin.site.register(Category)
admin.site.register(Company)
admin.site.register(Workers)
