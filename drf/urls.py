from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from mainapp.views import VacancyModelViewSet

router = routers.SimpleRouter()
router.register('vacancy', VacancyModelViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
] + router.urls
