from rest_framework import serializers
from auditApp.models.ResponseSousChapitre import ReponseSousChapitre

class ResponseSousChapitreSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReponseSousChapitre
        fields = '__all__'
