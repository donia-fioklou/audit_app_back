from rest_framework import serializers
from auditApp.models.Article import Article

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'
