from django.conf import settings
from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path, include
from django.conf.urls import url
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
   openapi.Info(
      title="IMG service API",
      default_version='v1',
      description="API for IMG service",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="info@img-service.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    #path(settings.ADMIN_URL, admin.site.urls),
    path('admin/', admin.site.urls),
    # API base url
    path("api/", include("config.api_router")),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    # API schema
    url(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    url(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    url(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
