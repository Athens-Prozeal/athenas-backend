# Generated by Django 5.0.6 on 2024-08-12 19:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inspection', '0004_excavationform_delete_exacavationform'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='excavationform',
            name='fields',
        ),
        migrations.DeleteModel(
            name='InspectionItem',
        ),
    ]
