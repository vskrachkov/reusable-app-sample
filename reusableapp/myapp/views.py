from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from myapp.models import get_model, RootModel
from myapp.seializers import AuthorSerializer, ArticleSerializer, \
    RootModelSerializer


class AuthorViewSet(viewsets.ModelViewSet):
    serializer_class = AuthorSerializer
    queryset = get_model('Author').objects.all()
    permission_classes = [AllowAny]


class ArticleViewSet(viewsets.ModelViewSet):
    serializer_class = ArticleSerializer()
    queryset = get_model('Article').objects.all()
    permission_classes = [AllowAny]


class RootViewSet(viewsets.ModelViewSet):
    serializer_class = RootModelSerializer
    queryset = RootModel.objects.all()
    permission_classes = [AllowAny]