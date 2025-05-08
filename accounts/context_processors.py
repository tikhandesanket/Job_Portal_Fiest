from .models import Profile

def user_profile(request):
    if request.user.is_authenticated:
        try:
            profile = request.user.profile
            return {'profile': profile}
        except Profile.DoesNotExist:
            return {'profile': None}
    return {'profile': None}
