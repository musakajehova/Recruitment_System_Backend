# Tests

## These are all the tests that I need to perform to check if the app works.

### models
CustomUser
- [] Candidate Register
- [] Recruiter Register

person
- [] create a profile
- [] update profile
countries
is admin
- [] create country
- [] view country
- [] edit counrty 
location
- [] create
- [] view 
- [] edit 
industry
- [] create
- [] view
- [] edit
company_profile
- [] create
- [] view
- [] edit
job_type
- [] create
- [] view
- [] edit
jobs
- [] create
- [] view
- [] edit
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