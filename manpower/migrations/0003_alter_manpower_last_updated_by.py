# Generated by Django 5.0.6 on 2024-07-19 18:53

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manpower', '0002_alter_manpower_date_alter_manpower_sub_contractor'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='manpower',
            name='last_updated_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='last_updated_manpowers', to=settings.AUTH_USER_MODEL),
        ),
    ]
