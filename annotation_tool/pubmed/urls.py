from django.conf.urls import url, include
from rest_framework import routers

from annotation_tool.pubmed import views

router = routers.DefaultRouter()
router.register('pubmed', views.PubmedViewSet)

urlpatterns = [
    url(r'^', include(router.urls))
]
