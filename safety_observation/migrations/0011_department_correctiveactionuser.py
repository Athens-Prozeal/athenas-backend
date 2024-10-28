# Generated by Django 5.0.6 on 2024-09-08 14:15

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0022_alter_worksiterole_role'),
        ('safety_observation', '0010_remove_safetyobservation_created_under_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=155)),
            ],
        ),
        migrations.CreateModel(
            name='CorrectiveActionUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='corrective_action_users', to=settings.AUTH_USER_MODEL)),
                ('work_site', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='authentication.worksite')),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='safety_observation.department')),
            ],
        ),
    ]
