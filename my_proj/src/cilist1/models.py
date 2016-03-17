# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin sqlcustom [app_label]'
# into your database.
from __future__ import unicode_literals

from django.db import models


class AboutThisApp(models.Model):
    sortorder = models.IntegerField(primary_key=True)
    about_fld = models.TextField()
    createdtime = models.DateTimeField(blank=True, null=True)
    updatedtime = models.DateTimeField(blank=True, null=True)

    class Meta:
        #managed = False
        db_table = 'about_this_app'

class Cilisting1(models.Model):
    #ft = models.CharField(max_length=22, blank=True, null=True)
    project_number = models.CharField(max_length=29)
    project_description = models.CharField(max_length=500, blank=True, null=True)
    owner = models.CharField(max_length=200, blank=True, null=True)
    planned_timing = models.DateField(blank=True, null=True)
    revised_timing = models.DateField(blank=True, null=True)
    estimated_cost = models.IntegerField(blank=True, null=True)
    savings_category = models.CharField(max_length=211, blank=True, null=True)
    annual_savings_dollars = models.CharField(max_length=20, blank=True, null=True)
    percent_complete = models.CharField(max_length=26, blank=True, null=True)
    comments = models.TextField(blank=True, null=True)
    originator = models.CharField(max_length=31, blank=True, null=True)
    team = models.CharField(max_length=600, blank=True, null=True)
    documents_complete = models.CharField(max_length=3, blank=True, null=True)
    one_time_savings = models.CharField(max_length=45, blank=True, null=True)
    hard_soft_savings = models.CharField(max_length=9, blank=True, null=True)
    soft_dollars = models.CharField(max_length=20, blank=True, null=True)
    il1_target_date = models.DateField(blank=True, null=True)
    il2_target_date = models.DateField(blank=True, null=True)
    il3_target_date = models.DateField(blank=True, null=True)
    il4_target_date = models.DateField(blank=True, null=True)
    il5_target_date = models.DateField(blank=True, null=True)
    wc_idea_date = models.DateField(blank=True, null=True)
    actual_implementation_date = models.DateField(blank=True, null=True)
    enter_in_wc = models.CharField(max_length=25, blank=True, null=True)
    area = models.CharField(max_length=99, blank=True, null=True)
    updatedtime = models.DateTimeField()
    id_wc = models.CharField(max_length=10, blank=True, null=True)
    environmental = models.CharField(max_length=23, blank=True, null=True)
    ease_of_implementation = models.CharField(max_length=27, blank=True, null=True)
    submit = models.CharField(max_length=10, blank=True, null=True)
    #line_num = models.IntegerField(blank=True, null=True)
    next_steps = models.CharField(max_length=987, blank=True, null=True)
    suggestion_status = models.CharField(max_length=99, blank=True, null=True)
    #ci_leader_1 = models.CharField(max_length=119, blank=True, null=True)
    group = models.CharField(max_length=99, blank=True, null=True)
    metric_impact = models.CharField(max_length=77, blank=True, null=True)
    gift_4_suggestion = models.CharField(max_length=10, blank=True, null=True)
    il_current = models.CharField(max_length=1, blank=True, null=True)
    createdtime = models.DateTimeField(blank=True, null=True)
    link = models.CharField(max_length=567)
    linkmore = models.CharField(max_length=9999)
    display = models.CharField(max_length=11)
    #idea_qtr_1 = models.IntegerField(db_column='idea_Qtr_1', blank=True, null=True)  # Field name made lowercase.
    #orginator_email = models.CharField(max_length=233, blank=True, null=True)
    ciid = models.AutoField(primary_key=True)
    #z_updatedtime = models.DateTimeField(db_column='z-updatedtime', blank=True, null=True)  # Field renamed to remove unsuitable characters.

    class Meta:
        #managed = False
        db_table = 'cilisting1'
        ordering = ["-ciid"]



