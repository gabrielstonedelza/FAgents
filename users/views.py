from django.shortcuts import render,get_object_or_404
from rest_framework import filters
from rest_framework.decorators import api_view, permission_classes
from rest_framework import viewsets, permissions, generics, status
from rest_framework.response import Response


from .models import User, OwnerProfile, AdminProfile, AgentProfile
from .serializers import UsersSerializer, OwnerProfileSerializer, AdminProfileSerializer, AgentProfileSerializer

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
def get_owners_profile(request):
    my_profile = OwnerProfile.objects.filter(user=request.user)
    serializer = OwnerProfileSerializer(my_profile, many=True)
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
def update_owner_profile(request):
    my_profile = OwnerProfile.objects.get(user=request.user)
    serializer = OwnerProfileSerializer(my_profile, data=request.data)
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


# get all supervisors
@api_view(['GET'])
@permission_classes([permissions.AllowAny])
def get_all_supervisors(request):
    supervisors = User.objects.filter(user_type="Owner")
    serializer = UsersSerializer(supervisors, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([permissions.AllowAny])
def get_all_agents(request):
    agents = User.objects.filter(user_type="Agent")
    serializer = UsersSerializer(agents, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([permissions.AllowAny])
def get_de_admin(request):
    agents = User.objects.filter(user_type="Administrator")
    serializer = UsersSerializer(agents, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([permissions.AllowAny])
def get_all_user(request):
    users = User.objects.exclude(id=request.user.id)
    serializer = UsersSerializer(users, many=True)
    return Response(serializer.data)

@api_view(['GET', 'PUT'])
@permission_classes([permissions.IsAuthenticated])
def update_blocked(request, id):
    user = get_object_or_404(User, id=id)
    serializer = UsersSerializer(user, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def get_all_blocked_users(request):
    users = User.objects.filter(user_blocked=True)
    serializer = UsersSerializer(users, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def get_supervisor_with_code(request,unique_code):
    user = User.objects.filter(agent_unique_code=unique_code)
    serializer = UsersSerializer(user, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def get_supervisor_with_code(request,unique_code):
    user = User.objects.filter(agent_unique_code=unique_code)
    serializer = UsersSerializer(user, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def get_owner_agents(request, supervisors_code):
    agents = User.objects.filter(owner=supervisors_code)
    serializer = UsersSerializer(agents, many=True)
    return Response(serializer.data)


@api_view(['GET', 'PUT'])
@permission_classes([permissions.IsAuthenticated])
def approve_user(request, id):
    user = get_object_or_404(User, id=id)
    serializer = UsersSerializer(user, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)