from rest_framework.views import APIView
from rest_framework.response import Response


class HelloWorld(APIView):
	"""Simple api view"""
	def get(self,request,format=None):
		"""Simple get request demo"""
		dict=['this is a demo response','APIView class','django rest framework']

		return Response({'message':'hello','dict':dict})