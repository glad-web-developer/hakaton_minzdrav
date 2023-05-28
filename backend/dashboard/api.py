from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination

from dashboard.models import Dashboard, Widget
from dashboard.serializers import DashboardSerializer, WidgetSerializer


class DashboardPagination(PageNumberPagination):
    page_size = 9
    page_size_query_param = 'count'
    max_page_size = 9


class WidgetViewSet(viewsets.ModelViewSet):
    queryset = Widget.objects.all()
    serializer_class = WidgetSerializer


class DashboardViewSet(viewsets.ModelViewSet):
    queryset = Dashboard.objects.all()
    serializer_class = DashboardSerializer
    pagination_class = DashboardPagination
