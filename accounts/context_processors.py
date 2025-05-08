from .models import Profile

def user_profile(request):
    profile = None
    if request.user.is_authenticated:
        profile, created = Profile.objects.get_or_create(user=request.user)
    return {'user_profile': profile}