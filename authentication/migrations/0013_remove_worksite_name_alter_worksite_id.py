# Generated by Django 5.0.6 on 2024-07-21 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0012_alter_worksiterole_role'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='worksite',
            name='name',
        ),
        migrations.AlterField(
            model_name='worksite',
            name='id',
            field=models.CharField(max_length=255, primary_key=True, serialize=False, unique=True),
        ),
    ]
