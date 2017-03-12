# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models

class UniversitydataCollegedata(models.Model):
    university = models.CharField(db_column='University', max_length=74, blank=True, null=True)  # Field name made lowercase.
    state = models.CharField(db_column='State', max_length=2, blank=True, null=True)  # Field name made lowercase.
    city = models.CharField(db_column='City', max_length=22, blank=True, null=True)  # Field name made lowercase.
    enrollment_undergrad = models.IntegerField(db_column='Enrollment_Undergrad', blank=True, null=True)  # Field name made lowercase.
    male = models.DecimalField(db_column='Male', max_digits=15, decimal_places=13, blank=True, null=True)  # Field name made lowercase.
    female = models.DecimalField(db_column='Female', max_digits=14, decimal_places=12, blank=True, null=True)  # Field name made lowercase.
    native_hawaiian_pacific_islander = models.DecimalField(db_column='Native_Hawaiian_Pacific_Islander', max_digits=3, decimal_places=1, blank=True, null=True)  # Field name made lowercase.
    american_indian_alaskan_native = models.DecimalField(db_column='American_Indian_Alaskan_Native', max_digits=3, decimal_places=1, blank=True, null=True)  # Field name made lowercase.
    multi_race_not_hispanic_latino = models.DecimalField(db_column='Multi_race_not_Hispanic_Latino', max_digits=3, decimal_places=1, blank=True, null=True)  # Field name made lowercase.
    asian = models.DecimalField(db_column='Asian', max_digits=3, decimal_places=1, blank=True, null=True)  # Field name made lowercase.
    white = models.DecimalField(db_column='White', max_digits=3, decimal_places=1, blank=True, null=True)  # Field name made lowercase.
    black_african_american = models.DecimalField(db_column='Black_African_American', max_digits=3, decimal_places=1, blank=True, null=True)  # Field name made lowercase.
    international = models.DecimalField(db_column='International', max_digits=3, decimal_places=1, blank=True, null=True)  # Field name made lowercase.
    hispanic_latino = models.DecimalField(db_column='Hispanic_Latino', max_digits=4, decimal_places=1, blank=True, null=True)  # Field name made lowercase.
    unknown = models.DecimalField(db_column='Unknown', max_digits=3, decimal_places=1, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'UniversityData_CollegeData'


class Statedemographics(models.Model):
    location = models.CharField(db_column='Location', max_length=20, blank=True, null=True)  # Field name made lowercase.
    white = models.DecimalField(db_column='White', max_digits=3, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    black = models.CharField(db_column='Black', max_length=4, blank=True, null=True)  # Field name made lowercase.
    hispanic = models.DecimalField(db_column='Hispanic', max_digits=3, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    asian = models.CharField(db_column='Asian', max_length=4, blank=True, null=True)  # Field name made lowercase.
    american_indian_alaska_native = models.CharField(db_column='American_Indian_Alaska_Native', max_length=4, blank=True, null=True)  # Field name made lowercase.
    native_hawaiian_other_pacific_islander = models.CharField(db_column='Native_Hawaiian_Other_Pacific_Islander', max_length=4, blank=True, null=True)  # Field name made lowercase.
    two_or_more_races = models.CharField(db_column='Two_Or_More_Races', max_length=4, blank=True, null=True)  # Field name made lowercase.
    total = models.IntegerField(db_column='Total', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'StateDemographics'


