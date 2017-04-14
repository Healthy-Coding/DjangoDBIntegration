from django.contrib import admin
from .models import UniversitydataCollegedata, Statedemographics


@admin.register(UniversitydataCollegedata)
class CollegeAdmin(admin.ModelAdmin):
    list_display = ('id', 'university', 'state_location')
    empty_value_display = '-empty-'

    def state_location(self, instance):
        return instance.state.location