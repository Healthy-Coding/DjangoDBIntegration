# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class Georgia(models.Model):
    name = models.CharField(db_column='Name', max_length=34, blank=True, null=True)  # Field name made lowercase.
    city = models.CharField(db_column='City', max_length=13, blank=True, null=True)  # Field name made lowercase.
    state = models.CharField(db_column='State', max_length=2, blank=True, null=True)  # Field name made lowercase.
    size = models.IntegerField(db_column='Size', blank=True, null=True)  # Field name made lowercase.
    amer_indian = models.DecimalField(db_column='Amer_Indian', max_digits=2, decimal_places=1, blank=True, null=True)  # Field name made lowercase.
    african_amer = models.DecimalField(db_column='African_Amer', max_digits=3, decimal_places=1, blank=True, null=True)  # Field name made lowercase.
    asian_pac_is = models.DecimalField(db_column='Asian_Pac_Is', max_digits=3, decimal_places=1, blank=True, null=True)  # Field name made lowercase.
    hispanic = models.DecimalField(db_column='Hispanic', max_digits=3, decimal_places=1, blank=True, null=True)  # Field name made lowercase.
    international = models.DecimalField(db_column='International', max_digits=3, decimal_places=1, blank=True, null=True)  # Field name made lowercase.
    white = models.DecimalField(db_column='White', max_digits=3, decimal_places=1, blank=True, null=True)  # Field name made lowercase.
    multi_race_not_hispanic_latino = models.DecimalField(max_digits=2, decimal_places=1, blank=True, null=True)
    unknown = models.DecimalField(db_column='Unknown', max_digits=2, decimal_places=1, blank=True, null=True)  # Field name made lowercase.
    women = models.DecimalField(db_column='Women', max_digits=3, decimal_places=1, blank=True, null=True)  # Field name made lowercase.
    men = models.DecimalField(db_column='Men', max_digits=3, decimal_places=1, blank=True, null=True)  # Field name made lowercase.

    def __str__(self):
        return self.name

    class Meta:
        managed = False
        db_table = 'Georgia'


