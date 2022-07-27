from django.contrib import admin
from django.urls import path, include

from weather import urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('weather.urls'))
]
