from django.contrib import admin
from home.models import patient_data
from home.models import User
from home.models import Hospitals


# Register your models here.

admin.site.register(patient_data)
admin.site.register(User)
admin.site.register(Hospitals)

