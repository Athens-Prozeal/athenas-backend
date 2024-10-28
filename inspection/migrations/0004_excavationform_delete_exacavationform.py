# Generated by Django 5.0.6 on 2024-08-12 19:35

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inspection', '0003_abstractinspection_exacavationform_delete_inspection'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExcavationForm',
            fields=[
                ('abstractinspection_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='inspection.abstractinspection')),
                ('project_name', models.CharField(max_length=155)),
                ('description', models.TextField()),
                ('date_of_checking', models.DateField()),
                ('ref_drawing_no', models.CharField(max_length=155)),
                ('underground_service_identified_via', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No'), ('N/A', 'N/A')], max_length=10)),
                ('underground_service_identified_via_remark', models.TextField(blank=True, null=True)),
                ('equipment_on_site', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No'), ('N/A', 'N/A')], max_length=10)),
                ('equipment_on_site_remark', models.TextField(blank=True, null=True)),
                ('excavation_extent_identified', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No'), ('N/A', 'N/A')], max_length=10)),
                ('excavation_extent_identified_remark', models.TextField(blank=True, null=True)),
                ('engineering_complete_for_trenching', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No'), ('N/A', 'N/A')], max_length=10)),
                ('engineering_complete_for_trenching_remark', models.TextField(blank=True, null=True)),
                ('soil_assessed', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No'), ('N/A', 'N/A')], max_length=10)),
                ('soil_assessed_remark', models.TextField(blank=True, null=True)),
                ('contaminated_soil_disposal', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No'), ('N/A', 'N/A')], max_length=10)),
                ('contaminated_soil_disposal_remark', models.TextField(blank=True, null=True)),
                ('other_specifications', models.TextField(blank=True, null=True)),
                ('soil_removed_or_protected', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No'), ('N/A', 'N/A')], max_length=10)),
                ('soil_removed_or_protected_remark', models.TextField(blank=True, null=True)),
                ('site_secured', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No'), ('N/A', 'N/A')], max_length=10)),
                ('site_secured_remark', models.TextField(blank=True, null=True)),
                ('exposed_services_protected', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No'), ('N/A', 'N/A')], max_length=10)),
                ('exposed_services_protected_remark', models.TextField(blank=True, null=True)),
                ('excavation_cuts_clean', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No'), ('N/A', 'N/A')], max_length=10)),
                ('excavation_cuts_clean_remark', models.TextField(blank=True, null=True)),
                ('removals_satisfactory', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No'), ('N/A', 'N/A')], max_length=10)),
                ('removals_satisfactory_remark', models.TextField(blank=True, null=True)),
                ('space_clean_organized', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No'), ('N/A', 'N/A')], max_length=10)),
                ('space_clean_organized_remark', models.TextField(blank=True, null=True)),
                ('contaminated_material_disposal', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No'), ('N/A', 'N/A')], max_length=10)),
                ('contaminated_material_disposal_remark', models.TextField(blank=True, null=True)),
                ('fields', models.ManyToManyField(to='inspection.inspectionitem')),
            ],
            bases=('inspection.abstractinspection',),
        ),
        migrations.DeleteModel(
            name='ExacavationForm',
        ),
    ]
