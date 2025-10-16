from django.urls import path, include
from .views import (RegisterView, LoginView, LogoutView, JobsListView, JobsListCreateView, DeleteJobsView, 
                    PersonListView, CountriesListCreateView, LocationListCreateView, IndustryListCreateView, 
                    CompanyListCreateView, JobTypeListCreatView)
from rest_framework import views

#TO do-list
#   Fix the api endpoints by adding <int:pk>/ for update and delete
urlpatterns= [
    path( 'register/', RegisterView.as_view(), name='register_view'),
    path( 'login/', LoginView.as_view(), name='login_view'),
    path( 'logout/', LogoutView.as_view(), name='logout_view'),
    path( 'jobs/', JobsListView.as_view(), name='jobs_view'),
    path( 'jobs/create/', JobsListCreateView.as_view(), name='jobsCreate_view'),
    path( 'jobs/delete/<int:pk>/', DeleteJobsView.as_view(), name='deleteJobs_view'),
    path( 'person/', PersonListView.as_view(), name='person_view'),
    path( 'person/create/', PersonListView.as_view(), name='person_create'),
    path( 'countries/', CountriesListCreateView.as_view(), name='countries_view'),
    path( 'countries/create/', CountriesListCreateView.as_view(), name='countriesCreate_view'),
    path( 'location/', LocationListCreateView.as_view(), name='location_view'),
    path( 'location/create/', LocationListCreateView.as_view(), name='locationCreate_view'),
    path( 'industry/', IndustryListCreateView.as_view(), name='industry_view'),
    path( 'industry/create/', IndustryListCreateView.as_view(), name='industryCreate_view'),
    path( 'company/', CompanyListCreateView.as_view(), name='company_view'),
    path( 'company/create/', CompanyListCreateView.as_view(), name='companyCreate_view'),
    path( 'jobtype/', JobTypeListCreatView.as_view(), name='jobType_view'),
    path( 'jobtype/create/', JobTypeListCreatView.as_view(), name='jobTypeCreate_view'), 
    path('api-token-auth/', views.obtain_auth_token)   
]
"""
RegisterView
LoginView
LogoutView
JobsListView
JobsListCreateView
DeleteJobsView
PersonListView
CountriesListCreateView
LocationListCreateView
IndustryListCreateView
CompanyListCreateView
JobTypeListCreatView
"""