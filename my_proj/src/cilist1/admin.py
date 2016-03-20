# vim: set fileencoding=utf-8 :
from django.contrib import admin

from . import models
from advanced_filters.admin import AdvancedFilterAdmin, AdminAdvancedFiltersMixin

class AboutThisAppAdmin(admin.ModelAdmin):

    list_display = ('sortorder', 'about_fld', 'createdtime', 'updatedtime')
    list_filter = ('createdtime', 'updatedtime')
    list_per_page = 10
    list_display_links = ('about_fld', 'sortorder')

    
class Cilisting1Admin( AdminAdvancedFiltersMixin, admin.ModelAdmin ):

 
    list_display = (
        #'ft',
        'project_number',
        'ciid',
        'project_description',
        'owner',
        'suggestion_status',
        'comments',
        'originator',
        'team',
        'wc_idea_date',
        #'revised_timing',
        #'estimated_cost',
        #'savings_category',
        'planned_timing',
        'annual_savings_dollars',
        'percent_complete',
        #'documents_complete',
        #'one_time_savings',
        #'hard_soft_savings',
        #'soft_dollars',
        #'il1_target_date',
        #'il2_target_date',
        #'il3_target_date',
        'il4_target_date',
        #'il5_target_date',
        'actual_implementation_date',
        #'enter_in_wc',
        #'area',
        'updatedtime',
        #'id_wc',
        
        #'environmental',
        #'ease_of_implementation',
        #'submit',
        #'line_num',
        #'next_steps',
        #'ci_leader_1',
        #'group',
        #'metric_impact',
        #'gift_4_suggestion',
        #'il_current',
        #'createdtime',
        #'link',
        #'linkmore',
        #'display',
        #'idea_qtr_1',
        #'orginator_email',
        #'z_updatedtime',
    )

    search_fields = (
        'project_number',
        'project_description',
        'owner',
        'estimated_cost',
        'savings_category',
        'annual_savings_dollars',
        'percent_complete',
        'comments',
        'originator',
        'team',
        'soft_dollars',
        'enter_in_wc',
        'area',
        'environmental',
        'ease_of_implementation',
        'submit',
        #'line_num',
        'next_steps',
        'suggestion_status',
        'group',
        'metric_impact',
#        'gift_4_suggestion',
#        'il_current',
        'link',
        'linkmore',
        'display',
#        'idea_qtr_1',
#        'orginator_email',
    )

    list_filter = (
        'wc_idea_date',
        'actual_implementation_date',
        # 'updatedtime',
        # 'createdtime',
        #'owner',
        #'originator',
        )

    # select from these fields in the advanced filter creation form
    advanced_filter_fields = (
        'owner',  'originator',  'project_number',

    )

    list_display_links = (
        'project_number',
        'ciid',
        'project_description',
    #       'owner',
    #       'suggestion_status',
    #       'comments'
    )

#set the number of entries on the grid...
list_per_page = 15


def _register(model, admin_class):
    admin.site.register(model, admin_class)


_register(models.AboutThisApp, AboutThisAppAdmin)
_register(models.Cilisting1, Cilisting1Admin)
