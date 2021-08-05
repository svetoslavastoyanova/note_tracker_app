from django.urls import path

from notes_tracker.profiles.views import create_profile, profile_details

urlpatterns = [
    path('', profile_details, name='profile details'),
    path('create/', create_profile, name='create profile'),


]