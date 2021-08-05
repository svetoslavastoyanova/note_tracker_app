from notes_tracker.notes.models import Note
from notes_tracker.profiles.models import Profile


def get_profile():
    return Profile.objects.first()


