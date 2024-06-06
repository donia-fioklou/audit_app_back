from rest_framework import serializers
from auditApp.models.SousChapitre import SousChapitre

class SousChapitreSerializer(serializers.ModelSerializer):
    class Meta:
        model = SousChapitre
        fields = '__all__'
