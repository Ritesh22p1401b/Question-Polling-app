from django.contrib import admin
from django.urls import path,include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('polls.urls')),
    path('user-auth/',include('user.urls')),
]
