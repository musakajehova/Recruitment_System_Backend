from django.shortcuts import render
from .serializers import (UserSerialzer, RegisterSerializer, jobsSerialzer, PersonSerializer, CountriesSerializer,
                            LocationSerializer, IndustrySerializer, Company_profileSerializer, Job_typeSerializer)

from rest_framework import viewsets
from rest_framework.generics import (ListCreateAPIView, RetrieveUpdateAPIView,RetrieveDestroyAPIView, ListAPIView, 
                                     CreateAPIView, GenericAPIView)
from django.contrib.auth import get_user_model 
from .models import CustomUser, person, jobs, countries, location, industry, company_profile, job_type

# Create your views here.
User = get_user_model()

###############################################################################################
"""Admin Views"""
class RegisterView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer

class LoginView(GenericAPIView):
    pass

class LogoutView(GenericAPIView):
    pass

###############################################################################################
"""Views for Jobs """
class JobsListView(ListAPIView):
    queryset = jobs.objects.all()
    serializer_class = jobsSerialzer

class JobsListCreateView(ListCreateAPIView):
    queryset = jobs.objects.all()
    serializer_class = jobsSerialzer

class DeleteJobsView(RetrieveDestroyAPIView):
    queryset = jobs.objects.all()
    serializer_class = jobsSerialzer
###############################################################################################
class PersonListView(ListAPIView):
    queryset = person.objects.all()
    serializer_class = PersonSerializer

class CountriesListCreateView(ListCreateAPIView):
    queryset = countries.objects.all()
    serializer_class = CountriesSerializer

class LocationListCreateView(ListCreateAPIView):
    queryset = location.objects.all()
    serializer_class = LocationSerializer

class IndustryListCreateView(ListCreateAPIView):
    queryset = industry.objects.all()
    serializer_class = IndustrySerializer

class CompanyListCreateView(ListCreateAPIView):
    queryset = company_profile.objects.all()
    serializer_class = Company_profileSerializer

class JobTypeListCreatView(ListCreateAPIView):
    queryset = job_type.objects.all()
    serializer_class = Job_typeSerializer
