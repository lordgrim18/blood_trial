from django.contrib import admin

# Register your models here.

from .models import Donor,Patient

admin.site.register(Donor)
admin.site.register(Patient)
