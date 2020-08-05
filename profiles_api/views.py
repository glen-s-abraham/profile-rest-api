from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from profiles_api import serializers

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