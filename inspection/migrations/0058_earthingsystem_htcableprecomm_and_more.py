# Generated by Django 5.0.6 on 2024-10-12 13:23

import django.db.models.deletion
import uuid
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0029_alter_correctiveactionuser_work_site'),
        ('inspection', '0057_rename_inverterroomorcontrolroombuilding_inverterorcontrolroombuilding'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='EarthingSystem',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('checked_by_date', models.DateField(auto_now_add=True)),
                ('witness_1_date', models.DateField(blank=True, null=True)),
                ('witness_1_signature', models.ImageField(blank=True, null=True, upload_to='inspection/signatures/')),
                ('witness_1_approved', models.BooleanField(default=False)),
                ('witness_2_date', models.DateField(blank=True, null=True)),
                ('witness_2_signature', models.ImageField(blank=True, null=True, upload_to='inspection/signatures/')),
                ('witness_2_approved', models.BooleanField(default=False)),
                ('witness_3_date', models.DateField(blank=True, null=True)),
                ('witness_3_signature', models.ImageField(blank=True, null=True, upload_to='inspection/signatures/')),
                ('witness_3_approved', models.BooleanField(default=False)),
                ('approval_status', models.CharField(choices=[('initiated', 'Initiated'), ('in_progress', 'In Progress'), ('approved', 'Approved')], default='initiated', max_length=15)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('last_updated_at', models.DateTimeField(auto_now=True)),
                ('name_of_client', models.CharField(max_length=155)),
                ('location', models.CharField(max_length=155)),
                ('date_of_test', models.DateField()),
                ('make', models.CharField(max_length=155)),
                ('range', models.CharField(max_length=155)),
                ('serial_no', models.CharField(max_length=155)),
                ('calibration_details', models.CharField(max_length=155)),
                ('data', models.JSONField()),
                ('observation_or_comments', models.TextField()),
                ('checked_by', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='%(class)s_checked_by', to=settings.AUTH_USER_MODEL)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='created_%(class)s', to=settings.AUTH_USER_MODEL)),
                ('last_updated_by', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='last_updated_%(class)s', to=settings.AUTH_USER_MODEL)),
                ('witness_1', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='%(class)s_witness_1', to=settings.AUTH_USER_MODEL)),
                ('witness_2', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='%(class)s_witness_2', to=settings.AUTH_USER_MODEL)),
                ('witness_3', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='%(class)s_witness_3', to=settings.AUTH_USER_MODEL)),
                ('work_site', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='authentication.worksite')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='HTCablePreComm',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('checked_by_date', models.DateField(auto_now_add=True)),
                ('witness_1_date', models.DateField(blank=True, null=True)),
                ('witness_1_signature', models.ImageField(blank=True, null=True, upload_to='inspection/signatures/')),
                ('witness_1_approved', models.BooleanField(default=False)),
                ('witness_2_date', models.DateField(blank=True, null=True)),
                ('witness_2_signature', models.ImageField(blank=True, null=True, upload_to='inspection/signatures/')),
                ('witness_2_approved', models.BooleanField(default=False)),
                ('witness_3_date', models.DateField(blank=True, null=True)),
                ('witness_3_signature', models.ImageField(blank=True, null=True, upload_to='inspection/signatures/')),
                ('witness_3_approved', models.BooleanField(default=False)),
                ('approval_status', models.CharField(choices=[('initiated', 'Initiated'), ('in_progress', 'In Progress'), ('approved', 'Approved')], default='initiated', max_length=15)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('last_updated_at', models.DateTimeField(auto_now=True)),
                ('name_of_client', models.CharField(max_length=155)),
                ('location', models.CharField(max_length=155)),
                ('date_of_test', models.DateField()),
                ('make', models.CharField(max_length=155)),
                ('cable_rating', models.CharField(max_length=155)),
                ('data', models.JSONField()),
                ('checked_by', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='%(class)s_checked_by', to=settings.AUTH_USER_MODEL)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='created_%(class)s', to=settings.AUTH_USER_MODEL)),
                ('last_updated_by', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='last_updated_%(class)s', to=settings.AUTH_USER_MODEL)),
                ('witness_1', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='%(class)s_witness_1', to=settings.AUTH_USER_MODEL)),
                ('witness_2', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='%(class)s_witness_2', to=settings.AUTH_USER_MODEL)),
                ('witness_3', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='%(class)s_witness_3', to=settings.AUTH_USER_MODEL)),
                ('work_site', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='authentication.worksite')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='InverterDutyTransformer',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('checked_by_date', models.DateField(auto_now_add=True)),
                ('witness_1_date', models.DateField(blank=True, null=True)),
                ('witness_1_signature', models.ImageField(blank=True, null=True, upload_to='inspection/signatures/')),
                ('witness_1_approved', models.BooleanField(default=False)),
                ('witness_2_date', models.DateField(blank=True, null=True)),
                ('witness_2_signature', models.ImageField(blank=True, null=True, upload_to='inspection/signatures/')),
                ('witness_2_approved', models.BooleanField(default=False)),
                ('witness_3_date', models.DateField(blank=True, null=True)),
                ('witness_3_signature', models.ImageField(blank=True, null=True, upload_to='inspection/signatures/')),
                ('witness_3_approved', models.BooleanField(default=False)),
                ('approval_status', models.CharField(choices=[('initiated', 'Initiated'), ('in_progress', 'In Progress'), ('approved', 'Approved')], default='initiated', max_length=15)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('last_updated_at', models.DateTimeField(auto_now=True)),
                ('drawing_or_specification_no', models.CharField(max_length=155)),
                ('serial_no', models.CharField(max_length=155)),
                ('site_location_or_area', models.CharField(max_length=155)),
                ('checklists', models.JSONField()),
                ('comments_or_remarks', models.TextField()),
                ('checked_by', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='%(class)s_checked_by', to=settings.AUTH_USER_MODEL)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='created_%(class)s', to=settings.AUTH_USER_MODEL)),
                ('last_updated_by', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='last_updated_%(class)s', to=settings.AUTH_USER_MODEL)),
                ('witness_1', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='%(class)s_witness_1', to=settings.AUTH_USER_MODEL)),
                ('witness_2', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='%(class)s_witness_2', to=settings.AUTH_USER_MODEL)),
                ('witness_3', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='%(class)s_witness_3', to=settings.AUTH_USER_MODEL)),
                ('work_site', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='authentication.worksite')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='SPVModules',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('checked_by_date', models.DateField(auto_now_add=True)),
                ('witness_1_date', models.DateField(blank=True, null=True)),
                ('witness_1_signature', models.ImageField(blank=True, null=True, upload_to='inspection/signatures/')),
                ('witness_1_approved', models.BooleanField(default=False)),
                ('witness_2_date', models.DateField(blank=True, null=True)),
                ('witness_2_signature', models.ImageField(blank=True, null=True, upload_to='inspection/signatures/')),
                ('witness_2_approved', models.BooleanField(default=False)),
                ('approval_status', models.CharField(choices=[('initiated', 'Initiated'), ('in_progress', 'In Progress'), ('approved', 'Approved')], default='initiated', max_length=15)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('last_updated_at', models.DateTimeField(auto_now=True)),
                ('drawing_or_specification_no', models.CharField(max_length=155)),
                ('site_location_or_area', models.CharField(max_length=155)),
                ('checklists', models.JSONField()),
                ('comments_or_remarks', models.TextField()),
                ('checked_by', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='%(class)s_checked_by', to=settings.AUTH_USER_MODEL)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='created_%(class)s', to=settings.AUTH_USER_MODEL)),
                ('last_updated_by', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='last_updated_%(class)s', to=settings.AUTH_USER_MODEL)),
                ('witness_1', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='%(class)s_witness_1', to=settings.AUTH_USER_MODEL)),
                ('witness_2', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='%(class)s_witness_2', to=settings.AUTH_USER_MODEL)),
                ('work_site', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='authentication.worksite')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
