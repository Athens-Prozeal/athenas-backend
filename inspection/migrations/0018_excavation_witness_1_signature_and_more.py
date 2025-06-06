# Generated by Django 5.0.6 on 2024-08-24 05:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inspection', '0017_alter_excavation_checked_by_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='excavation',
            name='witness_1_signature',
            field=models.ImageField(blank=True, null=True, upload_to='inspection/signatures/'),
        ),
        migrations.AddField(
            model_name='excavation',
            name='witness_2_signature',
            field=models.ImageField(blank=True, null=True, upload_to='inspection/signatures/'),
        ),
        migrations.AddField(
            model_name='excavation',
            name='witness_3_signature',
            field=models.ImageField(blank=True, null=True, upload_to='inspection/signatures/'),
        ),
    ]
