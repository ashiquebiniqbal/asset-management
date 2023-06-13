from rest_framework import serializers
from .models import Asset

class AssetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Asset
        fields = ['id', 'name', 'company', 'employee', 'condition', 'checked_out_at', 'checked_in_at']
