from rest_framework import serializers
from auditApp.models.Exigence import Exigence

class ExigenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exigence
        fields = '__all__'
