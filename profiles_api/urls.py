from django.urls import path,include
from rest_framework.routers import DefaultRouter
from profiles_api import views


routes=DefaultRouter()
routes.register('hello-viewset',views.HelloViewset,basename='hello-viewset')


urlpatterns=[
	path('hello-api/',views.HelloWorld.as_view()),
	path('',include(routes.urls)),
]