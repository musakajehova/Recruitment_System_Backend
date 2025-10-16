from django.db import models
from django.contrib.auth.models import AbstractUser 


# Create your models here.
################################################################
"""Create tokens for the exsisting users"""
#from django.contrib.auth.models import User
#from rest_framework.authtoken.models import Token

#for user in User.objects.all():
#    Token.objects.get_or_create(user=user)
##################################################################

class CustomUser(AbstractUser):
    first_name=models.CharField(max_length=100, blank=False, null=False)
    surname=models.CharField(max_length=100)

    def __str__(self):
        return f"{self.username}"


class person(models.Model):
    created_date=models.DateTimeField(auto_now_add=True)
    Date_of_birth=models.DateField()
    phone_no=models.CharField(max_length=15)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    id_no = models.CharField(max_length=20, unique=True, blank=False, null=False)

    def __str__(self):
        return f"Date of birth:{self.Date_of_birth} Phone no:{self.phone_no} ID Numner:{self.id_no}"

class countries(models.Model):
    country_id=models.AutoField(primary_key=True)
    country=models.CharField(max_length=100, unique=True, blank=False, null=False)
    date_created=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.country

class location(models.Model):
    location_id=models.AutoField(primary_key=True)
    country_id=models.ForeignKey(countries, on_delete=models.CASCADE, blank=False)
    city=models.CharField(max_length=100, blank=False)
    postal_code=models.CharField(max_length=20)
    geo_location=models.CharField(max_length=30)

    def __str__(self):
        return f"City:{self.city} Postal Code:{self.postal_code} Geo-Location:{self.geo_location}"

class industry(models.Model):
    industry_id=models.AutoField(primary_key=True)
    industry=models.CharField(max_length=100, unique=True, blank=False)
    date_created=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.industry

class company_profile(models.Model):
    company_id=models.AutoField(primary_key=True)
    company_name=models.CharField(max_length=200, blank=False, unique=True, null=False)
    company_website=models.URLField(max_length=200)
    industry_id=models.ForeignKey(industry, on_delete=models.CASCADE, related_name="company_profile")
    location_id=models.ForeignKey(location, on_delete=models.CASCADE, related_name="company_profile")
    date_created=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Company Name:{self.company_name} Company Website:{self.company_website}"

class job_type(models.Model):
    job_type_id=models.AutoField(primary_key=True)
    job_type=models.CharField(max_length=100, unique=True, blank=False)
    date_created=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Job Type:{self.job_type}"

class jobs(models.Model):
    job_id=models.AutoField(primary_key=True)
    title=models.CharField(max_length=200)
    description=models.TextField()
    location_id=models.ForeignKey(location, on_delete=models.CASCADE, related_name="jobs")
    industry_id=models.ForeignKey(industry, on_delete=models.CASCADE, related_name="jobs")
    job_type_id=models.ForeignKey(job_type, on_delete=models.CASCADE, related_name="jobs")
    company_id=models.ForeignKey(company_profile, on_delete=models.CASCADE, related_name="jobs")
    start_date=models.DateField()
    end_date=models.DateField()
    date_created=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Title:{self.title} Start Date:{self.start_date} End date:{self.end_date}"
    

