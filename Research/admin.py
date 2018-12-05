from django.contrib import admin
from .models import ResearchArticles
# Register your models here.
class ResearchArticlesAdmin(admin.ModelAdmin):
    list_display = ('Rtitle','Rauthor','Rpublish')
    list_filter = ('Rpublish','Rauthor')
    search_fields = ('Rtitle',"Rinstitution")
    raw_id_fields = ("Rauthor",)
    date_hierarchy = "Rpublish"
    ordering = ['Rpublish','Rauthor']
admin.site.register(ResearchArticles,ResearchArticlesAdmin)