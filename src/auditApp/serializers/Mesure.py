from rest_framework import serializers
from auditApp.models.Mesure import Mesure

class MesureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mesure
        fields = '__all__'
