from django.shortcuts import render
from .serializers import (UserSerialzer, RegisterSerializer, jobsSerialzer, PersonSerializer, CountriesSerializer,
                            LocationSerializer, IndustrySerializer, Company_profileSerializer, Job_typeSerializer)

from rest_framework import viewsets
from rest_framework.generics import (ListCreateAPIView, RetrieveUpdateAPIView,RetrieveDestroyAPIView, ListAPIView, 
                                     CreateAPIView, GenericAPIView)
from django.contrib.auth import get_user_model, authenticate
from .models import CustomUser, person, jobs, countries, location, industry, company_profile, job_type
from rest_framework.permissions import AllowAny
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.authtoken.models import Token

# Create your views here.
User = get_user_model()

class NormalPaginationSize(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100


###############################################################################################
"""Admin Views"""
class RegisterView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes  = [AllowAny]

class LoginView(GenericAPIView):
    permission_classes  = [AllowAny]

    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")
        user = authenticate(username=username, password=password)
        if user:
            token, _ = Token.objects.get_or_create(user=user)
            return Response({"token": token.key})
        return Response({"error": "Invalid credentials"}, status=400)
    pass

class LogoutView(GenericAPIView):
    permission_classes  = [AllowAny]
    pass

###############################################################################################
"""Views for Jobs """
class JobsListView(ListAPIView):
    queryset = jobs.objects.all()
    serializer_class = jobsSerialzer
    pagination_class = NormalPaginationSize

class JobsListCreateView(ListCreateAPIView):
    queryset = jobs.objects.all()
    serializer_class = jobsSerialzer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
    

class DeleteJobsView(RetrieveDestroyAPIView):
    queryset = jobs.objects.all()
    serializer_class = jobsSerialzer
###############################################################################################
"""Views for Person """
class PersonListView(ListCreateAPIView):
    queryset = person.objects.all()
    serializer_class = PersonSerializer

    def perform_create(self, serializer):
        serializer.save(user_id=self.request.user)

class Person(RetrieveUpdateAPIView):
    queryset = person.objects.all()
    serializer_class = PersonSerializer

###############################################################################################
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
