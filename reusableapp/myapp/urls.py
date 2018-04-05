from rest_framework import routers

from myapp.views import AuthorViewSet, ArticleViewSet

router = routers.SimpleRouter()
router.register(r'authors', AuthorViewSet)
router.register(r'articles', ArticleViewSet)
urlpatterns = router.urls
