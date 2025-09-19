from django.contrib import admin
from django.urls import path, include   # ✅ add include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('relationship/', include('relationship_app.urls')),
]

