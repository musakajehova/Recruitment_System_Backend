# Tests

## These are all the tests that I need to perform to check if the app works.

### models

CustomUser
- [x] Candidate Register
- [ ] Recruiter Register

login
- [x] login
- [x] logout

person
- [x] create a profile
- [ ] create a Recruiter
- [x] update profile
- [ ] update profile role

countries
- [x] create country
- [x] view country
- [x] edit counrty 

location
- [ ] create
- [ ] view 
- [ ] edit 
industry
- [ ] create
- [ ] view
- [ ] edit
company_profile
- [ ] create
- [ ] view
- [ ] edit
job_type
- [ ] create
- [ ] view
- [ ] edit
jobs
- [ ] create
- [ ] view
- [ ] edit
applications - still to be created 


path( 'register/', RegisterView.as_view(), name='register_view'),
    path( 'register/recruiter/<int:pk>/', RecruiterRegisterView.as_view(), name='recruiter_register_view'),

    path( 'login/', LoginView.as_view(), name='login_view'),
    path( 'logout/', LogoutView.as_view(), name='logout_view'),

    path( 'jobs/', JobsListView.as_view(), name='jobs_view'),
    path( 'jobs/create/', JobsListCreateView.as_view(), name='jobsCreate_view'),
    path( 'jobs/delete/<int:pk>/', DeleteJobsView.as_view(), name='deleteJobs_view'),
    path( 'jobs/update/<int:pk>/', JobsUpdateView.as_view(), name='UpdateJobs_view'),
    path( 'jobs/recruiter/<int:pk>/', JobsRecruiterView.as_view(), name='recruiterJobs_view'),

    
    path( 'person/', PersonListView.as_view(), name='person_view'),
    path( 'person/create/', PersonListView.as_view(), name='person_create'),
     path( 'person/admin_view/<int:pk>/', AdminPersonsView.as_view(), name='adminPerson_create'),

    path( 'countries/', CountriesListCreateView.as_view(), name='countries_view'),
    path( 'countries/create/', CountriesListCreateView.as_view(), name='countriesCreate_view'),
    path( 'countries/update/<int:pk>/', CountriesUpdateView.as_view(), name='countriesUpdate_view'),
    
    path( 'location/', LocationListCreateView.as_view(), name='location_view'),
    path( 'location/create/', LocationListCreateView.as_view(), name='locationCreate_view'),
    path( 'location/update/<int:pk>/', LocationUpdateView.as_view(), name='locationUpdate_view'),

    path( 'industry/', IndustryListCreateView.as_view(), name='industry_view'),
    path( 'industry/create/', IndustryListCreateView.as_view(), name='industryCreate_view'),
    path( 'industry/update/<int:pk>/', IndustryUpdateView.as_view(), name='industryUpdate_view'),
   
    path( 'company/', CompanyListCreateView.as_view(), name='company_view'),
    path( 'company/create/', CompanyListCreateView.as_view(), name='companyCreate_view'),
    path( 'company/update/<int:pk>/', CompanyUpdateView.as_view(), name='companyUpadate_view'),
    
### 
    jobtype/
    jobtype/create/
    jobtype/update/<int:pk>/ 

    api-token-auth



#test 
Authorization : Token <token-key>

register
{
    "username": "2",
    "email": "test@admin.com",
    "first_name": "test_1",
    "surname": "test_1",
    "password": "Alx#1"
}

login
{
    "username":"2",
    "password":"Alx#1"
}
returned
{"token":"7df118076a038e3b01a6660ba867b6488fd71069","user_id":4,"username":"2","email":"test@admin.com"}

logout
return
{
    "message": "Logged out successfully"
}

Person
{
    "Date_of_birth": "1992-10-19",
    "phone_no":"0746965372",
    "profile_picture": null,
    "id_no": "9210192546875123658"
}
return
{
        "user_id": "musa",
        "date_created": "2025-10-19T07:51:29.079587+02:00",
        "Date_of_birth": "1992-10-19",
        "phone_no": "0746965372",
        "profile_picture": null,
        "id_no": "9210192546875123658",
        "updated_at": "2025-10-19T07:51:29.079674+02:00",
        "role": "candidate"
}

Countries
{
    "country":"Botswana"
}
return
{
    "country_id":1,"country":"South Africa","date_created":"2025-10-19T12:57:15.316561+02:00"
}

Location
{
    "country_id": 1,
    "city": "Johannesburg",
    "postal_code": "2180",
    "geo_location": "151-2151-2135-3215"
}
return
{
    "location_id": 1,
    "country_id": 1,
    "city": "Johannesburg",
    "postal_code": "2180",
    "geo_location": "151-2151-2135-3215",
    "date_created": "2025-10-19T13:21:35.544996+02:00"
}

Industry
{
    "industry": "Mining"
}
return
{
    "industry_id": 1,
    "industry": "Mining",
    "date_created": "2025-10-19T13:38:36.539250+02:00"
}

Company
{
    "company_name": "AliMusaTrading",
    "company_website": "http://alimusatrading.com/",
    "industry_id": 1,
    "location_id": 1
}

{
    "company_id": 1,
    "company_name": "AliMusaTrading",
    "company_website": "http://alimusatrading.com/",
    "industry_id": 1,
    "location_id": 1,
    "date_created": "2025-10-19T13:45:07.088628+02:00",
    "updated_at": "2025-10-19T13:45:07.088646+02:00"
}
return
{
    "company_id": 1,
    "company_name": "AliMusaTrading",
    "company_website": "http://alimusatrading.com/",
    "industry_id": 1,
    "location_id": "City of Johannesburg",
    "date_created": "2025-10-19T13:45:07.088628+02:00",
    "updated_at": "2025-10-19T13:45:07.088646+02:00"
}

JobType
{
    "job_type": "Back-End Developer"
}
return
{
    "job_type_id": 1,
    "job_type": "Back-End Developer",
    "date_created": "2025-10-19T14:04:30.625843+02:00"
}

Jobs
{
    "title": "Data Analyst",
    "description": "Knlkanlknklknknlknlknlknvlkdsanvlksdanvlksdnvjkasdnvjsdhbavjkdsbvkjsdvn",
    "location_id": 1,
    "industry_id": 1,
    "job_type_id": 1,
    "company_id": 1,
    "start_date": "2025-12-10",
    "end_date": "2026-05-14"
}

{
    "job_id": 1,
    "title": "Data Analyst",
    "description": "Knlkanlknklknknlknlknlknvlkdsanvlksdanvlksdnvjkasdnvjsdhbavjkdsbvkjsdvn",
    "location_id": "City of Johannesburg",
    "industry_id": "Mining",
    "job_type_id": "Back-End Developer",
    "company_id": "AliMusaTrading",
    "start_date": "2025-12-10",
    "end_date": "2026-05-14",
    "date_created": "2025-10-19T14:17:03.299884+02:00",
    "author": "musa",
    "updated_at": "2025-10-19T14:17:03.299901+02:00"
}