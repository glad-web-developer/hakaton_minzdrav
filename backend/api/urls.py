from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from api.api import Login, Logout, CheckUser

urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/login/', Login.as_view(),),
    path('api/logout/', Logout.as_view()),
    path('api/check_user/', CheckUser.as_view()),


    # path('', TemplateView.as_view(template_name="index.html"))
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
