# accounts/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import RegisterForm, LoginForm
from django.contrib.auth.decorators import login_required
from .models import Profile

# Register View
def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            # Lazy import to avoid circular import
            from .models import Profile  
            Profile.objects.create(
                user=user,
                user_type=form.cleaned_data.get('user_type')
            )
            return redirect('home')  # Redirect to home or job list page
    else:
        form = RegisterForm()
    return render(request, 'accounts/register.html', {'form': form})

# Login View
def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            # import ipdb; ipdb.set_trace()
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('redirect_dashboard')  
    else:
        form = LoginForm()
    return render(request, 'accounts/login.html', {'form': form})

    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')  # Redirect to home or job list page
    else:
        form = LoginForm()
    return render(request, 'accounts/login.html', {'form': form})

# Home View (optional, for logged-in users)
@login_required
def home_view(request):
    return render(request, 'accounts/home.html')


@login_required
def redirect_dashboard(request):
    import ipdb; ipdb.set_trace()
    
    user = request.user
    if user.is_superuser:
        return redirect('admin_dashboard')  # Define this view for admin
    try:
        profile = user.profile
        if profile.user_type == 'applicant':
            return redirect('job_list')  # applicant → view jobs
        elif profile.user_type == 'recruiter':
            return redirect('job_create')  # recruiter → post job
    except Profile.DoesNotExist:
        return redirect('login')
    
def admin_dashboard(request):
    return render(request, 'accounts/admin_dashboard.html')
