from rest_framework.viewsets import ViewSet, ModelViewSet

from mainapp.models import Vacancy
from mainapp.serializers import VacancySerializer


class VacancyModelViewSet(ModelViewSet):
    queryset = Vacancy.objects.all()
    serializer_class = VacancySerializer
