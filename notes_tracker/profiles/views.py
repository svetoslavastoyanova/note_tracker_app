from django.shortcuts import render, redirect

from notes_tracker.core.profile_utils import get_profile
from notes_tracker.notes.models import Note
from notes_tracker.profiles.forms import CreateProfileForm
from notes_tracker.profiles.models import Profile


def create_profile(request):
    if request.method == 'POST':
        form = CreateProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = CreateProfileForm()

    context = {
        'form': form,
    }

    return render(request, 'home-no-profile.html', context)


def profile_details(request):
    profile = get_profile()
    context = {
        'profile': profile,
    }

    return render(request, 'profile.html', context)




