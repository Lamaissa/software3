from django.contrib import admin
from .models import(Manager)
from .models import(Team)
from .models import(Task)
# Register your models here.
#admin.site.register(Manager)
#admin.site.register(Team)
#admin.site.register(Task)
@admin.register(Manager)
class ManagerAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email')
    ordering = ('first_name', 'last_name', )

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    fields = (('title', 'priority', 'status'), 'due', 'manager', 'member_team','descript')
    list_display = ('title', 'manager', 'priority', 'due',)
    ordering = ('due', )
    list_filter = ('status', 'due')


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    fields = (('first_name', 'last_name'), 'evalutate', 'email', 'joined_us',)
    list_display = ('first_name', 'last_name', 'email', 'evalutate')
    ordering = ('first_name', 'last_name','evalutate',)
    list_filter = ('joined_us',)
