from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from profiles_api import serializers
from profiles_api import models
from profiles_api import permissions


class HelloWorld(APIView):
	"""Simple api view"""

	serializer_class=serializers.HelloSerializer

	def get(self,request,format=None):
		"""Simple get request demo"""
		dict=['this is a demo response','APIView class','django rest framework']

		return Response({'message':'hello','dict':dict})

	
	def post(self,request):
		"""Simple post request"""	
		input=self.serializer_class(data=request.data)
		if input.is_valid():
			name=input.validated_data.get('name')
			message=f'hello {name}!'
			return Response({'message':message})
		else:
			return Response(
							input.errors,
							status=status.HTTP_400_BAD_REQUEST
				)	

	
	def put(self,request,pk=None):
		"""Completely replaces an item"""
		return Response({'message':'PUT'})		


	def patch(self,request,pk=None):
		"""updates or replaces parts of an item"""
		return Response({'message':'PATCH'})		
		

	def delete(self,request,pk=None):
		"""Completely removes an item"""
		return Response({'message':'DELETE'})				


class HelloViewset(viewsets.ViewSet):
	"""View set class """

	serializer_class=serializers.HelloSerializer

	def list(self,request):
		"""Function for listing items"""
		return Response({'message':'Hello!!'})

	def retrieve(self,request,pk=None):
		"""Function for listing items"""
		return Response({'message':'GET'})	

	def create(self,request):
		serializer=self.serializer_class(data=request.data)
		if serializer.is_valid():
			name=serializer.validated_data.get('name')
			message=f'hello {name}'
			return Response({'message':message})
		else:
			return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)	

	def update(self,request,pk=None):
		"""Function for listing items"""
		return Response({'message':'PUT'})

	def partial_update(self,request,pk=None):
		"""Function for listing items"""
		return Response({'message':'PATCH'})	
	
	def destroy(self,request,pk=None):
		"""Function for listing items"""
		return Response({'message':'DELETE'})	


class UserProfileViewset(viewsets.ModelViewSet):
	"""Create and update user profile"""
	serializer_class=serializers.UserProfilesSerializer
	queryset=models.UserProfile.objects.all()
	authentication_classes = (TokenAuthentication,)
	permission_classes = (permissions.UpdateOwnProfile,)
	filter_backends = (filters.SearchFilter,)
	search_fields = ('name', 'email',)

    

class UserLoginApiView(ObtainAuthToken):
	"""Login view for profiles api"""
	renderer_classes=api_settings.DEFAULT_RENDERER_CLASSES

class UserProfilesFeedViewset(viewsets.ModelViewSet):
	"""create and manage user profile feed"""
	serializer_class=serializers.UserProfilesFeedSerializer
	authentication_classes=(TokenAuthentication,)
	queryset=models.UserProfilesFeed.objects.all()
	permission_classes=(
		permissions.UpdateOwnStatus,
		IsAuthenticatedOrReadOnly
		)

	def perform_create(self,serializer):
		"""adds to user_profile field current user"""
		serializer.save(user_profile=self.request.user) 
	