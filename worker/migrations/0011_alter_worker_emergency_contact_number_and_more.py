# Generated by Django 5.0.6 on 2024-09-07 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('worker', '0010_alter_worker_profile_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='worker',
            name='emergency_contact_number',
            field=models.CharField(max_length=15),
        ),
        migrations.AlterField(
            model_name='worker',
            name='mobile_number',
            field=models.CharField(max_length=15),
        ),
    ]
