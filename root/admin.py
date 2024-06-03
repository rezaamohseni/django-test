from django.contrib import admin
from .models import Team , Skill
class TeamAdmin(admin.ModelAdmin):
    list_display = ['title','status']
    list_filter = ['status']
    search_fields = ["title"]
    
    
admin.site.register(Team )
admin.site.register(Skill)