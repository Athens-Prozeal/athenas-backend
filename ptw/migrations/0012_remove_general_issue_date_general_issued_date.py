# Generated by Django 5.0.6 on 2024-10-21 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ptw', '0011_rename_accepted_by_general_approved_by_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='general',
            name='issue_date',
        ),
        migrations.AddField(
            model_name='general',
            name='issued_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
