# Generated by Django 5.0.6 on 2024-09-07 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('worker', '0009_alter_worker_profile_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='worker',
            name='profile_pic',
            field=models.ImageField(blank=True, null=True, upload_to='worker/profile_pictures/'),
        ),
    ]
