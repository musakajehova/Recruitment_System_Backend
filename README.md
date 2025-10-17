# Recruitment_System_Backend
This is a recruitment system that will connect job seeker and recruiters.


This is a simple recruitment job portal that will allow candidates to register a profile and then apply to jobs. Recruiters will be able to register a profile,  create jobs and search candidates.

## Authentication

The default authentica

## API Endpoints 
http://127.0.0.1:8000/
job_board/register/
job_board/login/
job_board/logout/
job_board/jobs/
    job_board/jobs/create/
    job_board/jobs/delete/
job_board/person/
job_board/countries/
    job_board/countries/create/
job_board/location/
    job_board/location/create/
job_board/industry/
    job_board/industry/create/
job_board/company/
    job_board/company/create/
job_board/jobtype/
    job_board/jobtype/create/

## Json
Templates you can use to interact with the API

### CustomUser:
{
    "username": ,
    "email": ,
    "name": ,
    "surname": ,
    "password": 
}

### person:
{
    "Date_of_birth":,
    "phone_no":,
    "profile_picture":, 
    "id_no": 
}
### countries:
{
    "country_id":,
    "country":,
}

### location:
{
    "location_id":,
    "country_id":,
    "city":,
    "postal_code":,
    "geo_location":
}
### industry:
{
    "industry_id": ,
    "industry": ,
}

### company_profile:
{
    "company_id": ,
    "company_name": ,
    "company_website": ,
    "industry_id": ,
    "location_id": ,
    "date_created": 
}

### job_type:
{
    "job_type_id": ,
    "job_type": ,
    "date_created": 
}

### jobs:
{
    "job_id": ,
    "title": ,
    "description": ,
    "location_id": ,
    "industry_id": ,
    "job_type_id": ,
    "company_id": ,
    "start_date": ,
    "end_date": ,
    "date_created": 
}

## models

Theses are all the models that where created.

User model has been extended and the first_name is now required 
CustomUser
    first_name
    surname

person
    created_date
    Date_of_birth
    profile_picture
    id_no

countries
    country_id      -primary_key
    country
    date_created

location
    location_id     -primary_key
    country_id      -ForeignKey
    city
    postal_code 
    geo_location 

industry
    industry_id     -primary_key
    industry
    date_created 

company_profile
    company_id      -primary_key
    industry_id     -ForeignKey
    location_id     -ForeignKey
    company_name  
    company_website 
    date_created 


job_type
    job_type_id     -primary_key
    job_type
    date_created 

jobs
    job_id          -primary_key
    title   
    description     
    location_id     -ForeignKey
    industry_id     -ForeignKey
    job_type_id     -ForeignKey
    company_id      -ForeignKey
    start_date
    end_date  
    date_created    
    author          -ForeignKey