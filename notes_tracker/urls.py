
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('notes_tracker.notes.urls')),
    path('profile/', include('notes_tracker.profiles.urls')),

]
