# Generated by Django 5.0.6 on 2024-07-15 11:22

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='WorkSite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'worksite',
            },
        ),
        migrations.CreateModel(
            name='WorkSiteRole',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(choices=[('epc', 'EPC'), ('client', 'Client'), ('subcontractor', 'Subcontractor')], max_length=50)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
                ('worksite', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='authentication.worksite')),
            ],
            options={
                'db_table': 'worksite_role',
            },
        ),
    ]
