from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from dcapi.models import Invocation

class InvocationAdmin(admin.ModelAdmin):
    list_display = ('caller_key','crp_records','nimsp_records','query_string','execution_time','timestamp')
admin.site.register(Invocation, InvocationAdmin)