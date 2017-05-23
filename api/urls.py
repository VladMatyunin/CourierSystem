from django.conf.urls import url, include
import views
from rest_framework import routers
router = routers.DefaultRouter()
router.register(r'orders', views.OrderViewSet)
router.register(r'groups', views.GroupViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]