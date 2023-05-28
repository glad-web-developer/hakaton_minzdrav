from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from api.api import Login, Logout, CheckUser, UrlImportTemplate, ImportExcel, MedDataSetLvApi

urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/login/', Login.as_view(), ),
    path('api/logout/', Logout.as_view()),
    path('api/check_user/', CheckUser.as_view()),

    path('api/url_import_template/<template_name>/', UrlImportTemplate.as_view()),
    path('api/url_import_template/', UrlImportTemplate.as_view()),

    path('api/import_excel/', ImportExcel.as_view()),

    path('api/med_data_set_api/', MedDataSetLvApi.as_view()),

    # path('', TemplateView.as_view(template_name="index.html"))
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
