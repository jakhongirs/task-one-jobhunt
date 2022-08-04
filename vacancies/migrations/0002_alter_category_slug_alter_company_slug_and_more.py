# Generated by Django 4.1 on 2022-08-04 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("vacancies", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="category",
            name="slug",
            field=models.CharField(blank=True, max_length=128, unique=True),
        ),
        migrations.AlterField(
            model_name="company",
            name="slug",
            field=models.CharField(blank=True, max_length=128, unique=True),
        ),
        migrations.AlterField(
            model_name="vacancy",
            name="slug",
            field=models.CharField(blank=True, max_length=128, unique=True),
        ),
    ]
