from django.contrib import admin

# Register your models here.
from .models import S_CURRICULUM,Students,Sign

# class couse(admin.ModelAdmin):
#     list_display = ['name', 'week_day', 'time_begin', 'time_end']
class StudentsAdmin(admin.ModelAdmin):
    list_display = ['name', 's_class', 's_id', 's_grade','s_photo','s_curriculum','s_time']
    def s_curriculum(self,obj):
        return [bt.s_curriculum for bt in obj.s_curriculum.all()]
    filter_horizontal=('s_curriculum',)

admin.site.register(S_CURRICULUM)
admin.site.register(Sign)
admin.site.register(Students,StudentsAdmin)
