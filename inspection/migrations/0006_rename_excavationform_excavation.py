# Generated by Django 5.0.6 on 2024-08-12 19:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inspection', '0005_remove_excavationform_fields_delete_inspectionitem'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ExcavationForm',
            new_name='Excavation',
        ),
    ]
