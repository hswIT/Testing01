from django.contrib import admin
from .models import ContectUs

# Register your models here.
class ContectUsAdmin(admin.ModelAdmin):
    list_display= ('name', 'email', 'subject','comment')


admin.site.register(ContectUs,ContectUsAdmin)