# Generated by Django 5.0.6 on 2024-09-08 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('safety_observation', '0011_department_correctiveactionuser'),
    ]

    operations = [
        migrations.AlterField(
            model_name='department',
            name='name',
            field=models.CharField(max_length=155, unique=True),
        ),
    ]
