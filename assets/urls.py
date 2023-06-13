from django.urls import path
from . import views
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .api import MyAPI

app_name = 'assets'

router = DefaultRouter()
router.register(r'my-api', MyAPI, basename='my-api')

urlpatterns = [
    path('', views.index, name='index'),
    path('subscribe/', views.subscribe, name='subscribe'),
    path('api/', include(router.urls)),
    path('checkout/', views.checkout, name='checkout'),
]

