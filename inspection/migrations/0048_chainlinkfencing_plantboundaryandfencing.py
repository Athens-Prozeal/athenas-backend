# Generated by Django 5.0.6 on 2024-09-26 16:34

import django.db.models.deletion
import uuid
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0028_alter_user_departments'),
        ('inspection', '0047_rename_comments_dcdb_comments_or_remarks'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ChainLinkFencing',
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
                ('project_name_and_capacity', models.CharField(max_length=155)),
                ('client_name', models.CharField(max_length=155)),
                ('epc_contractor_name', models.CharField(max_length=155)),
                ('date', models.DateField()),
                ('consultant_name', models.CharField(max_length=155)),
                ('location_or_area', models.CharField(max_length=155)),
                ('drawing_no', models.CharField(max_length=155)),
                ('contractor_name', models.CharField(max_length=155)),
                ('work_supervisor_name', models.CharField(max_length=155)),
                ('any_other_observation', models.TextField()),
                ('checklists', models.JSONField()),
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
            name='PlantBoundaryAndFencing',
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
                ('project_name_and_capacity', models.CharField(max_length=155)),
                ('client_name', models.CharField(max_length=155)),
                ('epc_contractor_name', models.CharField(max_length=155)),
                ('date', models.DateField()),
                ('consultant_name', models.CharField(max_length=155)),
                ('location_or_area', models.CharField(max_length=155)),
                ('contractor_name', models.CharField(max_length=155)),
                ('work_supervisor_name', models.CharField(max_length=155)),
                ('any_other_observation', models.TextField()),
                ('checklists', models.JSONField()),
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
    ]
