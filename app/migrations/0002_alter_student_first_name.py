# Generated by Django 4.1.7 on 2023-03-25 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='first_name',
            field=models.CharField(max_length=100),
        ),
    ]
