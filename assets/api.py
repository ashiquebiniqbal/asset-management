from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from .serializers import AssetSerializer
from .models import Asset
from rest_framework.viewsets import ModelViewSet




class MyAPI(ModelViewSet):
    queryset = Asset.objects.all()
    serializer_class = AssetSerializer


""" class MyAPI(APIView):
    def get(self, request):
        # Your API logic here
        data = {'message': 'This is a GET request'}
        return Response(data, status=status.HTTP_200_OK) """
