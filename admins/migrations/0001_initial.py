# Generated by Django 5.0.7 on 2024-07-20 07:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PlacementDrive',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=255)),
                ('job_role', models.CharField(max_length=255)),
                ('eligibility_criteria', models.TextField()),
                ('date', models.DateField()),
                ('time', models.TimeField()),
            ],
        ),
    ]
