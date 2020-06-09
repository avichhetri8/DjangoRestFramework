from django.urls import path, include
from rest_framework import routers

from RestExample import views
from RestExample.views import BookViewSet

router = routers.DefaultRouter()
router.register('book', BookViewSet)

urlpatterns = [
   path('', include(router.urls))
]
