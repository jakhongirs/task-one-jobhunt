from django.urls import path
from vacancies import views

urlpatterns = [
    path('', views.AllVacanciesView.as_view()),
]
