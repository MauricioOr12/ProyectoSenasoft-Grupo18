from django.contrib import admin
from django.urls import path
from django.conf import settings
from inicio import views
from django.conf.urls.static import static


urlpatterns = [
    path('', views.inicio, name="inicio"),

]

urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
