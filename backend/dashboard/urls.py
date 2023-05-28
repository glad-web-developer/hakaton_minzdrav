from rest_framework.routers import SimpleRouter

from dashboard.api import DashboardViewSet, WidgetViewSet

app_name = 'dashboard'

router = SimpleRouter()

router.register(r'widgets', WidgetViewSet)
router.register(r'', DashboardViewSet)

urlpatterns = router.urls
