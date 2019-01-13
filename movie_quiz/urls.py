"""movie_quiz URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.urls import include
from django.views.generic import TemplateView
from rest_framework_swagger.views import get_swagger_view
from rest_framework import routers
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_swagger_view(title='rest API')

router = routers.DefaultRouter()

schema_view = get_schema_view(
   openapi.Info(
      title="movie quze API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   validators=['flex', 'ssv'],
   public=True,
)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^quiz/', TemplateView.as_view(template_name='index.html')),
    url(r'^api/', include(router.urls)),
    url(r'^movie/', include('movie.urls')),
    url(r'^api/doc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

]



