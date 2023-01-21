from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', include('home.urls')),
    path('cashbook/', include('cashbook.urls')),
    path('goals', include('goals.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
