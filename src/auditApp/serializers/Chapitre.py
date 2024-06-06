from rest_framework import serializers
from auditApp.models.Chapitre import Chapitre

class ChapitreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chapitre
        fields = '__all__'
