# Generated by Django 5.0.6 on 2024-08-24 13:23

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inspection', '0020_rename_kid_excavation_id'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='excavation',
            name='checked_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='checked_inspections', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='excavation',
            name='witness_1',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='witnessed_inspections_1', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='excavation',
            name='witness_2',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='witnessed_inspections_2', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='excavation',
            name='witness_3',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='witnessed_inspections_3', to=settings.AUTH_USER_MODEL),
        ),
    ]
