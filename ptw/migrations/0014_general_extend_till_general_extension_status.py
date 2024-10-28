# Generated by Django 5.0.6 on 2024-10-21 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ptw', '0013_alter_general_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='general',
            name='extend_till',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='general',
            name='extension_status',
            field=models.CharField(choices=[('none', 'None'), ('requested', 'Requested'), ('approved', 'Approved'), ('rejected', 'Rejected')], default='none', max_length=15),
        ),
    ]
