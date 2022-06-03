from django.contrib import admin
from django.urls import path, include
from fcuser.views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('fcuser/', include('fcuser.urls')),
    path('board/', include('board.urls')),
    path('', home),
]
