from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'face'

urlpatterns = [
    path('', views.test, name='test'),
    path('media/', views.show, name='show'),
    path('face/', views.detect, name='detect')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)