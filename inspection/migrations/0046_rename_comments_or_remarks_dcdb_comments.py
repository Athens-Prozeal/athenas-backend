# Generated by Django 5.0.6 on 2024-09-26 14:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inspection', '0045_dcdb'),
    ]

    operations = [
        migrations.RenameField(
            model_name='dcdb',
            old_name='comments_or_remarks',
            new_name='comments',
        ),
    ]
