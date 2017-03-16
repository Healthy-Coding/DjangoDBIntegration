# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-03-12 21:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ListIndex', '0002_georgialargest15'),
    ]

    operations = [
        migrations.CreateModel(
            name='Statedemographics',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(blank=True, db_column='Location', max_length=20, null=True)),
                ('white', models.DecimalField(blank=True, db_column='White', decimal_places=2, max_digits=3, null=True)),
                ('black', models.CharField(blank=True, db_column='Black', max_length=4, null=True)),
                ('hispanic', models.DecimalField(blank=True, db_column='Hispanic', decimal_places=2, max_digits=3, null=True)),
                ('asian', models.CharField(blank=True, db_column='Asian', max_length=4, null=True)),
                ('american_indian_alaska_native', models.CharField(blank=True, db_column='American_Indian_Alaska_Native', max_length=4, null=True)),
                ('native_hawaiian_other_pacific_islander', models.CharField(blank=True, db_column='Native_Hawaiian_Other_Pacific_Islander', max_length=4, null=True)),
                ('two_or_more_races', models.CharField(blank=True, db_column='Two_Or_More_Races', max_length=4, null=True)),
                ('total', models.IntegerField(blank=True, db_column='Total', null=True)),
            ],
            options={
                'db_table': 'StateDemographics',
            },
        ),
        migrations.CreateModel(
            name='UniversitydataCollegedata',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('university', models.CharField(blank=True, db_column='University', max_length=74, null=True)),
                ('state', models.CharField(blank=True, db_column='State', max_length=2, null=True)),
                ('city', models.CharField(blank=True, db_column='City', max_length=22, null=True)),
                ('enrollment_undergrad', models.IntegerField(blank=True, db_column='Enrollment_Undergrad', null=True)),
                ('male', models.DecimalField(blank=True, db_column='Male', decimal_places=13, max_digits=15, null=True)),
                ('female', models.DecimalField(blank=True, db_column='Female', decimal_places=12, max_digits=14, null=True)),
                ('native_hawaiian_pacific_islander', models.DecimalField(blank=True, db_column='Native_Hawaiian_Pacific_Islander', decimal_places=1, max_digits=3, null=True)),
                ('american_indian_alaskan_native', models.DecimalField(blank=True, db_column='American_Indian_Alaskan_Native', decimal_places=1, max_digits=3, null=True)),
                ('multi_race_not_hispanic_latino', models.DecimalField(blank=True, db_column='Multi_race_not_Hispanic_Latino', decimal_places=1, max_digits=3, null=True)),
                ('asian', models.DecimalField(blank=True, db_column='Asian', decimal_places=1, max_digits=3, null=True)),
                ('white', models.DecimalField(blank=True, db_column='White', decimal_places=1, max_digits=3, null=True)),
                ('black_african_american', models.DecimalField(blank=True, db_column='Black_African_American', decimal_places=1, max_digits=3, null=True)),
                ('international', models.DecimalField(blank=True, db_column='International', decimal_places=1, max_digits=3, null=True)),
                ('hispanic_latino', models.DecimalField(blank=True, db_column='Hispanic_Latino', decimal_places=1, max_digits=4, null=True)),
                ('unknown', models.DecimalField(blank=True, db_column='Unknown', decimal_places=1, max_digits=3, null=True)),
            ],
            options={
                'db_table': 'UniversityData_CollegeData',
            },
        ),
    ]