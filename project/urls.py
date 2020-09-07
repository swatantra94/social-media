from django.contrib import admin
from django.urls import path,include
from reminderlist import urls
from autho import urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('reminderlist.urls')),
    path('auth/',include('autho.urls')),
]
