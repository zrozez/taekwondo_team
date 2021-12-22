from rest_framework import routers

from .views import NewsViewSet


router = routers.SimpleRouter()
router.register('news', NewsViewSet)
urlpatterns = []

urlpatterns += router.urls
