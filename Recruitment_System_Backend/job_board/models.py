from django.db import models
from django.contrib.auth.models import AbstractUser 

# Create your models here.
class CustomUser(AbstractUser):
    name=models.CharField(max_length=100)
    surname=models.CharField(max_length=100)
    pass


class person(models.Model):
    created_date=models.DateTimeField(auto_now_add=True)
    Date_of_birth=models.DateField()
    phone_no=models.CharField(max_length=15)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    id_no = models.IntegerField()

class countries(models.Model):
    country_id=models.AutoField(primary_key=True)
    country=models.CharField(max_length=100)
    date_created=models.DateTimeField(auto_now_add=True)

class location(models.Model):
    location_id=models.AutoField(primary_key=True)
    country_id=models.ForeignKey(countries, on_delete=models.CASCADE)
    city=models.CharField(max_length=100)
    postal_code=models.CharField(max_length=20)
    geo_location=models.CharField(max_length=30)

class industry(models.Model):
    industry_id=models.AutoField(primary_key=True)
    industry=models.CharField(max_length=100)
    date_created=models.DateTimeField(auto_now_add=True)


class company_profile(models.Model):
    company_id=models.AutoField(primary_key=True)
    company_name=models.CharField(max_length=200, related_name="company_profile")
    company_website=models.URLField(max_length=200, related_name="company_profile")
    industry_id=models.ForeignKey(industry, on_delete=models.CASCADE, related_name="company_profile")
    location_id=models.ForeignKey(location, on_delete=models.CASCADE, related_name="company_profile")
    date_created=models.DateTimeField(auto_now_add=True, related_name="company_profile")

class job_type(models.Model):
    job_type_id=models.AutoField(primary_key=True)
    job_type=models.CharField(max_length=100, related_name="job")
    date_created=models.DateTimeField(auto_now_add=True)

class jobs(models.Model):
    job_id=models.AutoField(primary_key=True)
    title=models.CharField(max_length=200, related_name="jobs")
    description=models.TextField(related_name="jobs")
    location_id=models.ForeignKey(location, on_delete=models.CASCADE, related_name="jobs")
    industry_id=models.ForeignKey(industry, on_delete=models.CASCADE, related_name="jobs")
    job_type_id=models.ForeignKey(job_type, on_delete=models.CASCADE, related_name="jobs")
    company_id=models.ForeignKey(company_profile, on_delete=models.CASCADE, related_name="jobs")
    start_date=models.DateField(related_name="jobs")
    end_date=models.DateField( related_name="jobs")
    date_created=models.DateTimeField(auto_now_add=True, related_name="jobs")


