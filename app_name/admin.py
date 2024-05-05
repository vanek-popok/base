from django.contrib import admin
from .models import Video

# Register your models here.
@admin.register(Video)
class videoadmin(admin.ModelAdmin):
    list_display = ('title',)