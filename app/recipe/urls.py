from django.urls import path, include
from rest_framework.routers import DefaultRouter

from recipe import views


#  Router register the appropriate url address for each action
#  or the API.
router = DefaultRouter()
router.register('tags', views.TagViewSet)

app_name = 'recipe'

urlpatterns = [
    path('', include(router.urls))
]