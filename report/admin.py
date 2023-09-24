from django.contrib import admin

from django.contrib.auth import get_user_model

from .models import Report

User = get_user_model()


@admin.register(Report)
class ReportAdmin(admin.ModelAdmin):
    list_display = ['user', 'diagnosed_with', 'lives_at', 'smoked', 'drank', 'around_sick']
