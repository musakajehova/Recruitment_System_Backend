from django.contrib import admin

# Register your models here.
from .models import CustomUser, person, jobs, countries, location, industry, company_profile, job_type
from django.contrib.auth.models import User
from rest_framework.authtoken.admin import TokenAdmin

admin.site.register(CustomUser)
admin.site.register(person)
admin.site.register(jobs)
admin.site.register(countries)
admin.site.register(location)
admin.site.register(industry)
admin.site.register(company_profile)
admin.site.register(job_type)
TokenAdmin.raw_id_fields = ['user']  #admin for token genenration