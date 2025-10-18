from django.urls import path, include
from .views import (RegisterView, LoginView, LogoutView, JobsListView, JobsListCreateView, DeleteJobsView, 
                    PersonListView, CountriesListCreateView, CountriesUpdateView, LocationListCreateView, LocationUpdateView,
                    IndustryListCreateView, IndustryUpdateView, CompanyListCreateView, CompanyUpdateView, JobTypeListCreatView, 
                    JobTypeUpdateView, RecruiterRegisterView, JobsUpdateView, AdminPersonsView)
from rest_framework.authtoken.views import obtain_auth_token


#TO do-list
#   Fix the api endpoints by adding <int:pk>/ for update and delete
urlpatterns= [
    path( 'register/', RegisterView.as_view(), name='register_view'),
    path( 'register/recruiter/<int:pk>/', RecruiterRegisterView.as_view(), name='recruiter_register_view'),

    path( 'login/', LoginView.as_view(), name='login_view'),
    path( 'logout/', LogoutView.as_view(), name='logout_view'),

    path( 'jobs/', JobsListView.as_view(), name='jobs_view'),
    path( 'jobs/create/', JobsListCreateView.as_view(), name='jobsCreate_view'),
    path( 'jobs/delete/<int:pk>/', DeleteJobsView.as_view(), name='deleteJobs_view'),
    path( 'jobs/update/<int:pk>/', JobsUpdateView.as_view(), name='UpdateJobs_view'),
    
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
    
    path( 'jobtype/', JobTypeListCreatView.as_view(), name='jobType_view'),
    path( 'jobtype/create/', JobTypeListCreatView.as_view(), name='jobTypeCreate_view'), 
    path( 'jobtype/update/<int:pk>/', JobTypeUpdateView.as_view(), name='jobTypeUpdate_view'), 

    path('api-token-auth/', obtain_auth_token)   
]