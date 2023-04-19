from django.shortcuts import render
from rest_framework import filters
from rest_framework.decorators import api_view, permission_classes
from rest_framework import viewsets, permissions, generics, status
from rest_framework.response import Response


from .models import User, SupervisorProfile, AdminProfile, AgentProfile
from .serializers import UsersSerializer, SupervisorProfileSerializer, AdminProfileSerializer, AgentProfileSerializer

def home(request):
    return render(request, "users/fnet_home.html")

@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def get_user(request):
    user = User.objects.filter(username=request.user.username)
    serializer = UsersSerializer(user, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def get_supervisors_profile(request):
    my_profile = SupervisorProfile.objects.filter(user=request.user)
    serializer = SupervisorProfileSerializer(my_profile, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def get_agents_profile(request):
    my_profile = AgentProfile.objects.filter(user=request.user)
    serializer = AgentProfileSerializer(my_profile, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def get_admins_profile(request):
    my_profile = AdminProfile.objects.filter(user=request.user)
    serializer = AdminProfileSerializer(my_profile, many=True)
    return Response(serializer.data)


@api_view(['GET', 'PUT'])
@permission_classes([permissions.IsAuthenticated])
def update_supervisor_profile(request):
    my_profile = SupervisorProfile.objects.get(user=request.user)
    serializer = SupervisorProfileSerializer(my_profile, data=request.data)
    if serializer.is_valid():
        serializer.save(user=request.user)
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT'])
@permission_classes([permissions.IsAuthenticated])
def update_agents_profile(request):
    my_profile = AgentProfile.objects.get(user=request.user)
    serializer = AgentProfileSerializer(my_profile, data=request.data)
    if serializer.is_valid():
        serializer.save(user=request.user)
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT'])
@permission_classes([permissions.IsAuthenticated])
def update_admins_profile(request):
    my_profile = AdminProfile.objects.get(user=request.user)
    serializer = AdminProfileSerializer(my_profile, data=request.data)
    if serializer.is_valid():
        serializer.save(user=request.user)
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT'])
@permission_classes([permissions.IsAuthenticated])
def update_user_details(request):
    user = User.objects.get(username=request.user.username)
    serializer = UsersSerializer(user, data=request.data)
    if serializer.is_valid():
        serializer.save(user=request.user)
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class GetAllAgents(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = UsersSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['username']

    def get_queryset(self):
        return User.objects.exclude(id=1).order_by('-date_joined')