from rest_framework import serializers
from profiles_api import models

class HelloSerializer(serializers.Serializer):
	"""Hello class serializer"""
	name=serializers.CharField(max_length=10)


class UserProfilesSerializer(serializers.ModelSerializer):
	"""Serializer for user profile"""


	class Meta:
		model=models.UserProfile
		fields=('id','email','name','password')
		extra_kwargs={

			'password':{
				'write_only':True,
				'style':{'input_type':'password'}
				
			}

		}	


	def create(self,validated_data):
		user=models.UserProfile.objects.create_user(
			email=validated_data['email'],
			name=validated_data['name'],
			password=validated_data['password']	
			)	
		return user


class UserProfilesFeedSerializer(serializers.ModelSerializer):
	"""Serializer for managing profile feed"""
	class Meta:
		model=models.UserProfilesFeed
		fields=('id','user_profile','feed_text','created_on')
		extra_kwargs={'user_profile':{'read_only':True}}
		