from rest_framework import serializers
from auditApp.models.SousArticle import SousArticle

class SousArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = SousArticle
        fields = '__all__'
