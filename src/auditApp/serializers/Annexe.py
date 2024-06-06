from rest_framework import serializers
from auditApp.models.Annexe import Annexe

class AnnexeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Annexe
        fields = '__all__'
