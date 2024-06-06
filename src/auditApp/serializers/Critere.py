from rest_framework import serializers
from auditApp.models.Critere import Critere

class CritereSerializer(serializers.ModelSerializer):
    class Meta:
        model = Critere
        fields = '__all__'
