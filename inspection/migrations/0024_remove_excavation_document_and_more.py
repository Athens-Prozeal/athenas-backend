# Generated by Django 5.0.6 on 2024-08-29 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inspection', '0023_antitermitetreatment_created_at_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='excavation',
            name='document',
        ),
        migrations.AddField(
            model_name='antitermitetreatment',
            name='checklists',
            field=models.JSONField(default={'sfd': 'gh'}),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='antitermitetreatment',
            name='comments',
            field=models.TextField(default='hj'),
            preserve_default=False,
        ),
    ]
