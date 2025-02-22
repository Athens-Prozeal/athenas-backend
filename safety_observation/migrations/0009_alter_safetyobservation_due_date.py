# Generated by Django 5.0.6 on 2024-09-07 12:43

import safety_observation.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('safety_observation', '0008_remove_safetyobservation_action_taken_or_required_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='safetyobservation',
            name='due_date',
            field=models.DateField(blank=True, null=True, validators=[safety_observation.validators.validate_due_date]),
        ),
    ]
