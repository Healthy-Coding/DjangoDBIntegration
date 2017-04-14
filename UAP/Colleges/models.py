# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class Collegeboard(models.Model):
    university = models.CharField(db_column='University', max_length=76, blank=True, null=True)  # Field name made lowercase.
    city = models.CharField(db_column='City', max_length=23, blank=True, null=True)  # Field name made lowercase.
    state = models.CharField(db_column='State', max_length=2, blank=True, null=True)  # Field name made lowercase.
    white = models.DecimalField(db_column='White', max_digits=3, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    hispanic_latino = models.DecimalField(db_column='Hispanic_Latino', max_digits=3, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    black_african_american = models.DecimalField(db_column='Black_African_American', max_digits=3, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    multi_race = models.DecimalField(db_column='Multi_Race', max_digits=3, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    asian = models.DecimalField(db_column='Asian', max_digits=3, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    unknown = models.DecimalField(db_column='Unknown', max_digits=3, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    non_resident_alien = models.DecimalField(db_column='Non_Resident_Alien', max_digits=3, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    american_indian_alaskan_native = models.DecimalField(db_column='American_Indian_Alaskan_Native', max_digits=3, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    native_hawaiian_pacific_islander = models.DecimalField(db_column='Native_Hawaiian_Pacific_Islander', max_digits=3, decimal_places=2, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CollegeBoard'


class Collegepictures(models.Model):
    university_name = models.CharField(db_column='University_Name', max_length=76, blank=True, null=True)  # Field name made lowercase.
    url = models.CharField(db_column='URL', max_length=394, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CollegePictures'


class Statedemographics(models.Model):
    location = models.CharField(db_column='Location', primary_key=True, max_length=13)  # Field name made lowercase.
    white = models.DecimalField(db_column='White', max_digits=3, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    black_african_american = models.CharField(db_column='Black', max_length=4, blank=True, null=True)  # Field name made lowercase.
    hispanic_latino = models.DecimalField(db_column='Hispanic', max_digits=3, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    asian = models.CharField(db_column='Asian', max_length=4, blank=True, null=True)  # Field name made lowercase.
    american_indian_alaskan_native = models.CharField(db_column='American_Indian_Alaska_Native', max_length=4, blank=True, null=True)  # Field name made lowercase.
    native_hawaiian_pacific_islander = models.CharField(db_column='Native_Hawaiian_Other_Pacific_Islander', max_length=4, blank=True, null=True)  # Field name made lowercase.
    multi_race = models.CharField(db_column='Two_Or_More_Races', max_length=4, blank=True, null=True)  # Field name made lowercase.
    total = models.IntegerField(db_column='Total', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'StateDemographics'


class UniversitydataCollegedata(models.Model):
    university = models.CharField(db_column='University', max_length=74, blank=True, null=True)  # Field name made lowercase.
    state = models.ForeignKey(Statedemographics, models.DO_NOTHING, db_column='State', blank=True, null=True)  # Field name made lowercase.
    city = models.CharField(db_column='City', max_length=22, blank=True, null=True)  # Field name made lowercase.
    enrollment_undergrad = models.IntegerField(db_column='Enrollment_Undergrad', blank=True, null=True)  # Field name made lowercase.
    male = models.DecimalField(db_column='Male', max_digits=4, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    female = models.DecimalField(db_column='Female', max_digits=4, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    native_hawaiian_pacific_islander = models.DecimalField(db_column='Native_Hawaiian_Pacific_Islander', max_digits=3, decimal_places=1, blank=True, null=True)  # Field name made lowercase.
    american_indian_alaskan_native = models.DecimalField(db_column='American_Indian_Alaskan_Native', max_digits=3, decimal_places=1, blank=True, null=True)  # Field name made lowercase.
    multi_race = models.DecimalField(db_column='Multi_Race', max_digits=3, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    asian = models.DecimalField(db_column='Asian', max_digits=3, decimal_places=1, blank=True, null=True)  # Field name made lowercase.
    white = models.DecimalField(db_column='White', max_digits=3, decimal_places=1, blank=True, null=True)  # Field name made lowercase.
    black_african_american = models.DecimalField(db_column='Black_African_American', max_digits=3, decimal_places=1, blank=True, null=True)  # Field name made lowercase.
    international = models.DecimalField(db_column='International', max_digits=3, decimal_places=1, blank=True, null=True)  # Field name made lowercase.
    hispanic_latino = models.DecimalField(db_column='Hispanic_Latino', max_digits=3, decimal_places=1, blank=True, null=True)  # Field name made lowercase.
    unknown = models.DecimalField(db_column='Unknown', max_digits=3, decimal_places=1, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        verbose_name = "College Data"
        db_table = 'UniversityData_CollegeData'


    def getState(self):
        return self.state.location

    def get_absolute_url(self):
        return "/colleges/%s/" % self.id



class Scorecard(models.Model):
    scorecard_id = models.AutoField(primary_key=True)
    unitid = models.IntegerField(db_column='UNITID')  # Field name made lowercase.
    opeid = models.IntegerField(db_column='OPEID')  # Field name made lowercase.
    opeid6 = models.IntegerField(db_column='OPEID6')  # Field name made lowercase.
    instnm = models.CharField(db_column='INSTNM', max_length=255, blank=True, null=True)  # Field name made lowercase.
    city = models.CharField(db_column='CITY', max_length=25, blank=True, null=True)  # Field name made lowercase.
    stabbr = models.CharField(db_column='STABBR', max_length=5, blank=True, null=True)  # Field name made lowercase.
    insturl = models.CharField(db_column='INSTURL', max_length=255, blank=True, null=True)  # Field name made lowercase.
    npcurl = models.CharField(db_column='NPCURL', max_length=255, blank=True, null=True)  # Field name made lowercase.
    hcm2 = models.IntegerField(db_column='HCM2')  # Field name made lowercase.
    preddeg = models.IntegerField(db_column='PREDDEG')  # Field name made lowercase.
    control = models.IntegerField(db_column='CONTROL')  # Field name made lowercase.
    locale = models.IntegerField(db_column='LOCALE')  # Field name made lowercase.
    hbcu = models.IntegerField(db_column='HBCU')  # Field name made lowercase.
    pbi = models.IntegerField(db_column='PBI')  # Field name made lowercase.
    annhi = models.IntegerField(db_column='ANNHI')  # Field name made lowercase.
    tribal = models.IntegerField(db_column='TRIBAL')  # Field name made lowercase.
    aanapii = models.IntegerField(db_column='AANAPII')  # Field name made lowercase.
    hsi = models.IntegerField(db_column='HSI')  # Field name made lowercase.
    nanti = models.IntegerField(db_column='NANTI')  # Field name made lowercase.
    menonly = models.IntegerField(db_column='MENONLY')  # Field name made lowercase.
    womenonly = models.IntegerField(db_column='WOMENONLY')  # Field name made lowercase.
    relaffil = models.CharField(db_column='RELAFFIL', max_length=5, blank=True, null=True)  # Field name made lowercase.
    satvr25 = models.CharField(db_column='SATVR25', max_length=5, blank=True, null=True)  # Field name made lowercase.
    satvr75 = models.CharField(db_column='SATVR75', max_length=5, blank=True, null=True)  # Field name made lowercase.
    satmt25 = models.CharField(db_column='SATMT25', max_length=5, blank=True, null=True)  # Field name made lowercase.
    satmt75 = models.CharField(db_column='SATMT75', max_length=5, blank=True, null=True)  # Field name made lowercase.
    satwr25 = models.CharField(db_column='SATWR25', max_length=5, blank=True, null=True)  # Field name made lowercase.
    satwr75 = models.CharField(db_column='SATWR75', max_length=5, blank=True, null=True)  # Field name made lowercase.
    satvrmid = models.CharField(db_column='SATVRMID', max_length=5, blank=True, null=True)  # Field name made lowercase.
    satmtmid = models.CharField(db_column='SATMTMID', max_length=5, blank=True, null=True)  # Field name made lowercase.
    satwrmid = models.CharField(db_column='SATWRMID', max_length=5, blank=True, null=True)  # Field name made lowercase.
    actcm25 = models.CharField(db_column='ACTCM25', max_length=5, blank=True, null=True)  # Field name made lowercase.
    actcm75 = models.CharField(db_column='ACTCM75', max_length=5, blank=True, null=True)  # Field name made lowercase.
    acten25 = models.CharField(db_column='ACTEN25', max_length=5, blank=True, null=True)  # Field name made lowercase.
    acten75 = models.CharField(db_column='ACTEN75', max_length=5, blank=True, null=True)  # Field name made lowercase.
    actmt25 = models.CharField(db_column='ACTMT25', max_length=5, blank=True, null=True)  # Field name made lowercase.
    actmt75 = models.CharField(db_column='ACTMT75', max_length=5, blank=True, null=True)  # Field name made lowercase.
    actwr25 = models.CharField(db_column='ACTWR25', max_length=5, blank=True, null=True)  # Field name made lowercase.
    actwr75 = models.CharField(db_column='ACTWR75', max_length=5, blank=True, null=True)  # Field name made lowercase.
    actcmmid = models.CharField(db_column='ACTCMMID', max_length=5, blank=True, null=True)  # Field name made lowercase.
    actenmid = models.CharField(db_column='ACTENMID', max_length=5, blank=True, null=True)  # Field name made lowercase.
    actmtmid = models.CharField(db_column='ACTMTMID', max_length=5, blank=True, null=True)  # Field name made lowercase.
    actwrmid = models.CharField(db_column='ACTWRMID', max_length=5, blank=True, null=True)  # Field name made lowercase.
    sat_avg = models.CharField(db_column='SAT_AVG', max_length=5, blank=True, null=True)  # Field name made lowercase.
    sat_avg_all = models.CharField(db_column='SAT_AVG_ALL', max_length=5, blank=True, null=True)  # Field name made lowercase.
    pcip01 = models.CharField(db_column='PCIP01', max_length=6, blank=True, null=True)  # Field name made lowercase.
    pcip03 = models.CharField(db_column='PCIP03', max_length=6, blank=True, null=True)  # Field name made lowercase.
    pcip04 = models.CharField(db_column='PCIP04', max_length=6, blank=True, null=True)  # Field name made lowercase.
    pcip05 = models.CharField(db_column='PCIP05', max_length=6, blank=True, null=True)  # Field name made lowercase.
    pcip09 = models.CharField(db_column='PCIP09', max_length=6, blank=True, null=True)  # Field name made lowercase.
    pcip10 = models.CharField(db_column='PCIP10', max_length=6, blank=True, null=True)  # Field name made lowercase.
    pcip11 = models.CharField(db_column='PCIP11', max_length=6, blank=True, null=True)  # Field name made lowercase.
    pcip12 = models.CharField(db_column='PCIP12', max_length=6, blank=True, null=True)  # Field name made lowercase.
    pcip13 = models.CharField(db_column='PCIP13', max_length=6, blank=True, null=True)  # Field name made lowercase.
    pcip14 = models.CharField(db_column='PCIP14', max_length=6, blank=True, null=True)  # Field name made lowercase.
    pcip15 = models.CharField(db_column='PCIP15', max_length=6, blank=True, null=True)  # Field name made lowercase.
    pcip16 = models.CharField(db_column='PCIP16', max_length=6, blank=True, null=True)  # Field name made lowercase.
    pcip19 = models.CharField(db_column='PCIP19', max_length=6, blank=True, null=True)  # Field name made lowercase.
    pcip22 = models.CharField(db_column='PCIP22', max_length=6, blank=True, null=True)  # Field name made lowercase.
    pcip23 = models.CharField(db_column='PCIP23', max_length=6, blank=True, null=True)  # Field name made lowercase.
    pcip24 = models.CharField(db_column='PCIP24', max_length=6, blank=True, null=True)  # Field name made lowercase.
    pcip25 = models.CharField(db_column='PCIP25', max_length=6, blank=True, null=True)  # Field name made lowercase.
    pcip26 = models.CharField(db_column='PCIP26', max_length=6, blank=True, null=True)  # Field name made lowercase.
    pcip27 = models.CharField(db_column='PCIP27', max_length=6, blank=True, null=True)  # Field name made lowercase.
    pcip29 = models.CharField(db_column='PCIP29', max_length=6, blank=True, null=True)  # Field name made lowercase.
    pcip30 = models.CharField(db_column='PCIP30', max_length=6, blank=True, null=True)  # Field name made lowercase.
    pcip31 = models.CharField(db_column='PCIP31', max_length=6, blank=True, null=True)  # Field name made lowercase.
    pcip38 = models.CharField(db_column='PCIP38', max_length=6, blank=True, null=True)  # Field name made lowercase.
    pcip39 = models.CharField(db_column='PCIP39', max_length=6, blank=True, null=True)  # Field name made lowercase.
    pcip40 = models.CharField(db_column='PCIP40', max_length=6, blank=True, null=True)  # Field name made lowercase.
    pcip41 = models.CharField(db_column='PCIP41', max_length=6, blank=True, null=True)  # Field name made lowercase.
    pcip42 = models.CharField(db_column='PCIP42', max_length=6, blank=True, null=True)  # Field name made lowercase.
    pcip43 = models.CharField(db_column='PCIP43', max_length=6, blank=True, null=True)  # Field name made lowercase.
    pcip44 = models.CharField(db_column='PCIP44', max_length=6, blank=True, null=True)  # Field name made lowercase.
    pcip45 = models.CharField(db_column='PCIP45', max_length=6, blank=True, null=True)  # Field name made lowercase.
    pcip46 = models.CharField(db_column='PCIP46', max_length=6, blank=True, null=True)  # Field name made lowercase.
    pcip47 = models.CharField(db_column='PCIP47', max_length=6, blank=True, null=True)  # Field name made lowercase.
    pcip48 = models.CharField(db_column='PCIP48', max_length=6, blank=True, null=True)  # Field name made lowercase.
    pcip49 = models.CharField(db_column='PCIP49', max_length=6, blank=True, null=True)  # Field name made lowercase.
    pcip50 = models.CharField(db_column='PCIP50', max_length=6, blank=True, null=True)  # Field name made lowercase.
    pcip51 = models.CharField(db_column='PCIP51', max_length=6, blank=True, null=True)  # Field name made lowercase.
    pcip52 = models.CharField(db_column='PCIP52', max_length=6, blank=True, null=True)  # Field name made lowercase.
    pcip54 = models.CharField(db_column='PCIP54', max_length=6, blank=True, null=True)  # Field name made lowercase.
    distanceonly = models.IntegerField(db_column='DISTANCEONLY')  # Field name made lowercase.
    ugds = models.CharField(db_column='UGDS', max_length=5, blank=True, null=True)  # Field name made lowercase.
    white = models.CharField(db_column='UGDS_WHITE', max_length=6, blank=True, null=True)  # Field name made lowercase.
    black_african_american = models.CharField(db_column='UGDS_BLACK', max_length=6, blank=True, null=True)  # Field name made lowercase.
    hispanic_latino = models.CharField(db_column='UGDS_HISP', max_length=6, blank=True, null=True)  # Field name made lowercase.
    asian = models.CharField(db_column='UGDS_ASIAN', max_length=6, blank=True, null=True)  # Field name made lowercase.
    american_indian_alaskan_native = models.CharField(db_column='UGDS_AIAN', max_length=6, blank=True, null=True)  # Field name made lowercase.
    native_hawaiian_pacific_islander = models.CharField(db_column='UGDS_NHPI', max_length=6, blank=True, null=True)  # Field name made lowercase.
    multi_race = models.CharField(db_column='UGDS_2MOR', max_length=6, blank=True, null=True)  # Field name made lowercase.
    ugds_nra = models.CharField(db_column='UGDS_NRA', max_length=6, blank=True, null=True)  # Field name made lowercase.
    ugds_unkn = models.CharField(db_column='UGDS_UNKN', max_length=6, blank=True, null=True)  # Field name made lowercase.
    pptug_ef = models.CharField(db_column='PPTUG_EF', max_length=6, blank=True, null=True)  # Field name made lowercase.
    curroper = models.IntegerField(db_column='CURROPER')  # Field name made lowercase.
    npt4_pub = models.CharField(db_column='NPT4_PUB', max_length=5, blank=True, null=True)  # Field name made lowercase.
    npt4_priv = models.CharField(db_column='NPT4_PRIV', max_length=5, blank=True, null=True)  # Field name made lowercase.
    npt41_pub = models.CharField(db_column='NPT41_PUB', max_length=5, blank=True, null=True)  # Field name made lowercase.
    npt42_pub = models.CharField(db_column='NPT42_PUB', max_length=5, blank=True, null=True)  # Field name made lowercase.
    npt43_pub = models.CharField(db_column='NPT43_PUB', max_length=5, blank=True, null=True)  # Field name made lowercase.
    npt44_pub = models.CharField(db_column='NPT44_PUB', max_length=5, blank=True, null=True)  # Field name made lowercase.
    npt45_pub = models.CharField(db_column='NPT45_PUB', max_length=5, blank=True, null=True)  # Field name made lowercase.
    npt41_priv = models.CharField(db_column='NPT41_PRIV', max_length=5, blank=True, null=True)  # Field name made lowercase.
    npt42_priv = models.CharField(db_column='NPT42_PRIV', max_length=5, blank=True, null=True)  # Field name made lowercase.
    npt43_priv = models.CharField(db_column='NPT43_PRIV', max_length=5, blank=True, null=True)  # Field name made lowercase.
    npt44_priv = models.CharField(db_column='NPT44_PRIV', max_length=5, blank=True, null=True)  # Field name made lowercase.
    npt45_priv = models.CharField(db_column='NPT45_PRIV', max_length=5, blank=True, null=True)  # Field name made lowercase.
    pctpell = models.CharField(db_column='PCTPELL', max_length=6, blank=True, null=True)  # Field name made lowercase.
    ret_ft4 = models.CharField(db_column='RET_FT4', max_length=6, blank=True, null=True)  # Field name made lowercase.
    ret_ftl4 = models.CharField(db_column='RET_FTL4', max_length=6, blank=True, null=True)  # Field name made lowercase.
    ret_pt4 = models.CharField(db_column='RET_PT4', max_length=6, blank=True, null=True)  # Field name made lowercase.
    ret_ptl4 = models.CharField(db_column='RET_PTL4', max_length=6, blank=True, null=True)  # Field name made lowercase.
    pctfloan = models.CharField(db_column='PCTFLOAN', max_length=6, blank=True, null=True)  # Field name made lowercase.
    ug25abv = models.CharField(db_column='UG25ABV', max_length=6, blank=True, null=True)  # Field name made lowercase.
    md_earn_wne_p10 = models.CharField(db_column='MD_EARN_WNE_P10', max_length=25, blank=True, null=True)  # Field name made lowercase.
    gt_25k_p6 = models.CharField(db_column='GT_25K_P6', max_length=25, blank=True, null=True)  # Field name made lowercase.
    grad_debt_mdn_supp = models.CharField(db_column='GRAD_DEBT_MDN_SUPP', max_length=25, blank=True, null=True)  # Field name made lowercase.
    grad_debt_mdn10yr_supp = models.CharField(db_column='GRAD_DEBT_MDN10YR_SUPP', max_length=25, blank=True, null=True)  # Field name made lowercase.
    rpy_3yr_rt_supp = models.CharField(db_column='RPY_3YR_RT_SUPP', max_length=25, blank=True, null=True)  # Field name made lowercase.
    c150_l4_pooled_supp = models.CharField(db_column='C150_L4_POOLED_SUPP', max_length=25, blank=True, null=True)  # Field name made lowercase.
    c150_4_pooled_supp = models.CharField(db_column='C150_4_POOLED_SUPP', max_length=25, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'scorecard'