from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('quickdrop/', include('quickdrop.urls')),  # Added trailing slash here
]