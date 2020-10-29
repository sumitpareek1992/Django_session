from django.contrib import admin
from main.models import Department, Students
from django.contrib.auth.models import Group

# Register your models here.
class StudentA(admin.ModelAdmin):
    exclude = ("email",)
    list_display = ("name", "age")
    list_filter = ("age",)
admin.site.register(Department)
admin.site.register(Students, StudentA)
admin.site.unregister(Group)

admin.site.site_header = "ITM University"