from django.urls import path,include
from rest_framework.routers import DefaultRouter
from profiles_api import views


routes=DefaultRouter()
routes.register('hello-viewset',views.HelloViewset,basename='hello-viewset')
routes.register('profiles',views.UserProfileViewset)
routes.register('feed',views.UserProfilesFeedViewset)

urlpatterns=[
	path('hello-api/',views.HelloWorld.as_view()),
	path('login/',views.UserLoginApiView.as_view()),
	path('',include(routes.urls)),
]