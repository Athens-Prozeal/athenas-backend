# Generated by Django 5.0.6 on 2024-07-20 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('worker', '0002_rename_registered_under_worker_created_under'),
    ]

    operations = [
        migrations.AddField(
            model_name='worker',
            name='designation',
            field=models.CharField(default='Worker', max_length=255),
        ),
    ]
