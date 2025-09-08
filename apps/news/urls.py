from .views import NewsViewSet
from django.urls import include , path
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register(r'news',NewsViewSet,basename="news")

urlpatterns = router.urls
