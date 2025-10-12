from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import CustomUser, person, jobs, countries, location, industry, company_profile, job_type
from rest_framework.authtoken.models import Token

User = get_user_model()

class UserSerialzer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'name', 'surname']

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password','name', 'surname']

    def create(self, validated_data):
        user = get_user_model().objects.create_user(
            username=validated_data['username'],
            email=validated_data.get('email'),
            password=validated_data['password'],
            name=validated_data['name'],
            surname=validated_data['surname'],
        )
        # create token for new user
        Token.objects.create(user=user)
        return user
    
class jobsSerialzer(serializers.ModelSerializer):
    company_name = serializers.CharField(source='company_profile.company_name', read_only=True)
    industry = serializers.CharField(source='industry.industry', read_only=True)
    location = serializers.CharField(source='location.city', read_only=True)
    job_type = serializers.CharField(source='job_type.job_type', read_only=True)
    
    class Meta:
        model = jobs
        fields = ['job_id', 'title', 'description', 'location', 'industry', 
                  'job_type', 'company_name', 'start_date', 'end_date', 'date_created']
        
class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = person
        fields = ['created_date', 'Date_of_birth', 'phone_no', 'profile_picture', 'id_no']

class CountriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = countries   
        fields = ['country_id', 'country', 'date_created']

class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = location
        fields = ['location_id', 'country_id', 'city', 'postal_code', 'geo_location']

        
class IndustrySerializer(serializers.ModelSerializer):
    class Meta:
        model = industry
        fields = ['industry_id' , 'industry' , 'date_created']

        
class Company_profileSerializer(serializers.ModelSerializer):
    class Meta:
        model = company_profile
        fields = ['company_id', 'company_name', 'company_website', 'industry_id', 'location_id', 'date_created']
        
class Job_typeSerializer(serializers.ModelSerializer):
    class Meta:
        model = job_type
        fields = ['job_type_id', 'job_type', 'date_created']

#Remember to update serializer to pull actual names rather than id