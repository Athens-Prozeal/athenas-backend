# Generated by Django 5.0.6 on 2024-08-20 08:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inspection', '0015_remove_excavation_witness_1_approval_status_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='excavation',
            name='checked_by_date',
            field=models.DateField(),
        ),
    ]
