from rest_framework import serializers

from myapp.models import get_model, RootModel


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_model('Author')
        fields = '__all__'


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_model('Article')
        fields = '__all__'


class RootModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = RootModel
        fields = '__all__'
