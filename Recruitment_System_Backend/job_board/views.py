from django.shortcuts import render
from .serializers import (UserSerialzer, RegisterSerializer, RecruiterPersonSerializer, jobsSerialzer, PersonSerializer, CountriesSerializer,
                            LocationSerializer, IndustrySerializer, Company_profileSerializer, Job_typeSerializer, ApplicationSerializer)

from rest_framework import viewsets, filters
from rest_framework.generics import (ListCreateAPIView, RetrieveUpdateAPIView,RetrieveDestroyAPIView, ListAPIView, 
                                     CreateAPIView, GenericAPIView)
from django.contrib.auth import get_user_model, authenticate
from .models import CustomUser, person, jobs, countries, location, industry, company_profile, job_type, applications
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from .permissions import IsRecruiter, IsAdministator
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.exceptions import ValidationError

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

class RecruiterRegisterView(RetrieveUpdateAPIView):
    """Only admin users can register Recruiters"""
    queryset = person.objects.all()
    serializer_class = RecruiterPersonSerializer
    permission_classes = [IsAuthenticated, IsAdminUser, IsAdministator]
    filter_backends = [filters.OrderingFilter]

class LoginView(GenericAPIView):
    permission_classes  = [AllowAny]

    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")
        user = authenticate(username=username, password=password)
        
        if user:
            token, _ = Token.objects.get_or_create(user=user)
            return Response({
                "token": token.key,
                "user_id": user.id,
                "username": user.username,
                "email": user.email})
        return Response({"error": "Invalid credentials"}, status=400)

class LogoutView(GenericAPIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        request.user.auth_token.delete()
        return Response({'message': 'Logged out successfully'}, status=200)

###############################################################################################
"""Views for Jobs """
class JobsListView(ListAPIView):
    queryset = jobs.objects.all()
    serializer_class = jobsSerialzer
    permission_classes = [IsAuthenticated]
    pagination_class = NormalPaginationSize
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['date_created', 'updated_at']

class JobsListCreateView(ListCreateAPIView):
    queryset = jobs.objects.all()
    serializer_class = jobsSerialzer
    #permission_classes = [IsAuthenticated, IsRecruiter, IsAdministator, IsAdminUser]
    permission_classes = [IsAuthenticated, IsRecruiter]
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['date_created', 'updated_at']

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class JobsRecruiterView(RetrieveUpdateAPIView):
    queryset = jobs.objects.all()
    serializer_class = jobsSerialzer
    permission_classes = [IsAuthenticated, IsRecruiter]
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['date_created', 'updated_at']

    def get_queryset(self):
        """
        This view should only return the jobs created by the recruiter
        """
        user = self.request.user
        return jobs.objects.filter(author=user)

class JobsUpdateView(RetrieveUpdateAPIView):
    queryset = jobs.objects.all()
    serializer_class = jobsSerialzer
    permission_classes = [IsAuthenticated, IsRecruiter]
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['date_created', 'updated_at']
    

class DeleteJobsView(RetrieveDestroyAPIView):
    queryset = jobs.objects.all()
    serializer_class = jobsSerialzer
    permission_classes = [IsAuthenticated, IsAdministator, IsAdminUser]
###############################################################################################
"""Views for Person """
class PersonListView(ListCreateAPIView):
    queryset = person.objects.all()
    serializer_class = PersonSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [filters.OrderingFilter]

    def perform_create(self, serializer):
        serializer.save(user_id=self.request.user)

    def get_queryset(self):
        """
        This view should only return the profile for login user
        """
        user = self.request.user
        return person.objects.filter(user_id=user)
        #remember to include an if statement for user authentication between admin and user


class AdminPersonsUpdate(RetrieveUpdateAPIView):
    """Only admin users can access all persons fields"""
    queryset = person.objects.all()
    serializer_class = PersonSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['date_created', 'updated_at']

class AdminPersonsView(ListAPIView):
    """Only admin users can access all persons fields"""
    queryset = person.objects.all()
    serializer_class = PersonSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['date_created', 'updated_at']

###############################################################################################
"""Only AdminUser can access these"""
class CountriesListCreateView(ListCreateAPIView):
    queryset = countries.objects.all()
    serializer_class = CountriesSerializer

class CountriesUpdateView(RetrieveUpdateAPIView):
    queryset = countries.objects.all()
    serializer_class = CountriesSerializer

class LocationListCreateView(ListCreateAPIView):
    queryset = location.objects.all()
    serializer_class = LocationSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['country_id']

class LocationUpdateView(RetrieveUpdateAPIView):
    queryset = location.objects.all()
    serializer_class = LocationSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['country_id']

class IndustryListCreateView(ListCreateAPIView):
    queryset = industry.objects.all()
    serializer_class = IndustrySerializer

class IndustryUpdateView(RetrieveUpdateAPIView):
    queryset = industry.objects.all()
    serializer_class = IndustrySerializer

class CompanyListCreateView(ListCreateAPIView):
    queryset = company_profile.objects.all()
    serializer_class = Company_profileSerializer

class CompanyUpdateView(RetrieveUpdateAPIView):
    queryset = company_profile.objects.all()
    serializer_class = Company_profileSerializer

class JobTypeListCreatView(ListCreateAPIView):
    queryset = job_type.objects.all()
    serializer_class = Job_typeSerializer

class JobTypeUpdateView(RetrieveUpdateAPIView):
    queryset = job_type.objects.all()
    serializer_class = Job_typeSerializer

class ApplicationsCreateListView(ListCreateAPIView):
    queryset = applications.objects.all()
    serializer_class = ApplicationSerializer
    permission_classes = [IsAuthenticated]
    search_fields =['job_id']
    ordering_fields = ['date_created', 'updated_at', 'jobs_id']

    def perform_create(self, serializer):
        user = self.request.user
        person = getattr(user, 'person', None)

        if not person:
            raise ValidationError("User does not have a related person profile.")

        serializer.save(user_id=user, person_id=person)
    
    def get_queryset(self):
        """
        Candidate views their own applications
        """
        user = self.request.user
        return applications.objects.filter(user_id=user)

class ApplicationsListView(ListAPIView):
    queryset = applications.objects.all()
    serializer_class = ApplicationSerializer
    permission_classes = [IsAuthenticated]
    search_fields =['job_id']
    ordering_fields = ['date_created', 'updated_at', 'jobs_id']
