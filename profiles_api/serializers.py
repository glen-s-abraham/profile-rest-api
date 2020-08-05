from rest_framework import serializers


class HelloSerializer(serializers.Serializer):
	"""Hello class serializer"""
	name=serializers.CharField(max_length=10)