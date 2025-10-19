from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import CustomUser, person, jobs, countries, location, industry, company_profile, job_type, applications
from rest_framework.authtoken.models import Token

User = get_user_model()

class UserSerialzer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'surname']

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password','first_name', 'surname']

    def create(self, validated_data):
        user = get_user_model().objects.create_user(
            username=validated_data['username'],
            email=validated_data.get('email'),
            password=validated_data['password'],
            first_name=validated_data['first_name'],
            surname=validated_data['surname'],
        )
        # create token for new user
        Token.objects.create(user=user)
        return user
    
class jobsSerialzer(serializers.ModelSerializer):
    company_name = serializers.CharField(source='company_id.company_name', read_only=True)
    industry = serializers.CharField(source='industry_id.industry', read_only=True)
    location = serializers.CharField(source='location_id.city', read_only=True)
    job_type = serializers.CharField(source='job_type_id.job_type', read_only=True)
    author = serializers.ReadOnlyField(source='author.username')
    
    class Meta:
        model = jobs
        fields = ['job_id', 'title', 'description', 'location_id', 'location', 'industry_id', 'industry',
                  'job_type_id', 'job_type', 'company_id', 'company_name', 'start_date', 'end_date', 'date_created',
                    'author','updated_at']
        read_only_fields = ['date_created']
        
class PersonSerializer(serializers.ModelSerializer):
    user_id = serializers.ReadOnlyField(source='user_id.username')

    class Meta:
        model = person
        fields = ['user_id', 'date_created', 'Date_of_birth', 'phone_no', 'profile_picture', 'id_no', 'updated_at', 'role']
        read_only_fields = ['date_created', 'user_id', 'role']

class RecruiterPersonSerializer(serializers.ModelSerializer):
    user_id = serializers.ReadOnlyField(source='user_id.username')

    class Meta:
        model = person
        fields = ['user_id', 'date_created', 'Date_of_birth', 'phone_no', 'profile_picture', 'id_no', 'updated_at', 'role']
        read_only_fields = ['user_id', 'date_created', 'Date_of_birth', 'phone_no', 'profile_picture', 'id_no', 'updated_at']

class CountriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = countries   
        fields = ['country_id', 'country', 'date_created']
        read_only_fields = ['date_created']

class LocationSerializer(serializers.ModelSerializer):
    country_id = serializers.CharField(source='country_id.country', read_only=True)

    class Meta:
        model = location
        fields = ['location_id', 'country_id', 'city', 'postal_code', 'geo_location', 'date_created']
        read_only_fields = ['date_created']

        
class IndustrySerializer(serializers.ModelSerializer):
    class Meta:
        model = industry
        fields = ['industry_id' , 'industry' , 'date_created']
        read_only_fields = ['date_created']

        
class Company_profileSerializer(serializers.ModelSerializer):
    location_id = serializers.CharField(source='location_id.city', read_only=True)
    
    class Meta:
        model = company_profile
        fields = ['company_id', 'company_name', 'company_website', 'industry_id', 'location_id', 'date_created', 'updated_at']
        read_only_fields = ['date_created'] 
        
class Job_typeSerializer(serializers.ModelSerializer):
    class Meta:
        model = job_type
        fields = ['job_type_id', 'job_type', 'date_created']
        read_only_fields = ['date_created']

#application
class ApplicationSerializer(serializers.ModelSerializer):
    user_id = serializers.ReadOnlyField(source='user_id.first_name')
    jobs_id = serializers.PrimaryKeyRelatedField(queryset=jobs.objects.all())
    person_id = serializers.ReadOnlyField(source='person_id.id')
    dateOfBirth = serializers.ReadOnlyField(source='person_id.Date_of_birth')
    phoneNo = serializers.ReadOnlyField(source='person_id.phone_no')
    idNno = serializers.ReadOnlyField(source='person_id.id_no')

    class Meta:
        model = applications
        fields = [ 'application_id', 'user_id', 'jobs_id', 'person_id', 'status', 'dateOfBirth', 'phoneNo', 'idNno',
                  'updated_at', 'date_created']
        read_only_fields = ['updated_at', 'date_created']