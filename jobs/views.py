from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import Job
from accounts.models import Profile
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render, redirect
from jobs.forms import JobForm
from .models import Job, UserJob


@login_required
def job_list(request):
    query = request.GET.get('q', '')
    user = request.user
    profile = Profile.objects.get(user=user)

    jobs_qs = Job.objects.filter(posted_by=request.user)
    using_dummy_data = not jobs_qs.exists()
    applied_job_ids = UserJob.objects.filter(user=user).values_list('job_id', flat=True)
    print(f"applied_job_ids: {applied_job_ids}")
    if using_dummy_data:
        jobs = [
            {
                 'id': 11,
                'title': 'Software Developer',
                'description': 'Develop and maintain software applications.',
                'salary': '8,00,000',
                'location': 'Mumbai, India'
            },
            {
                 'id': 112,
                'title': 'Full Stack Developer',
                'description': 'Work on frontend and backend systems.',
                'salary': '10,00,000',
                'location': 'Bangalore, India'
            },
        ]
        if query:
             filtered = [job for job in jobs if query.lower() in job['title'].lower()]
             jobsList = filtered if filtered else jobs  # fallback to all jobs if none matched
        else:
            jobsList = Job.objects.all() or jobs
    else:
        if query:
            jobsList = jobs_qs.filter(title__icontains=query)
        else:
            jobsList = jobs_qs

    return render(request, 'jobs/job_list.html', {
        'jobs': jobsList,
        'profile': profile,
        'query': query,
        'applied_job_ids':applied_job_ids,
    })



@login_required
def job_create(request):
    user = request.user
    profile = Profile.objects.get(user=user)
    # import ipdb; ipdb.set_trace()
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        salary = request.POST.get('salary')
        location = request.POST.get('location')
        category = request.POST.get('category')
        company = request.POST.get('company')

        # Save job
        Job.objects.create(
            title=title,
            description=description,
            salary=salary,
            location=location,
            category=category,
            company=company,
            posted_by=request.user
        )

        return redirect('job_list')  # Make sure 'job_list' is the correct URL name

    return render(request, 'jobs/job_create.html',{'profile': profile})



@login_required
def apply_job(request, job_id):
    job = get_object_or_404(Job, id=job_id)
    user = request.user
    profile = Profile.objects.get(user=user)
    if not UserJob.objects.filter(user=request.user, job=job).exists():
        UserJob.objects.create(user=request.user, job=job)
    return redirect("job_list")   


@login_required
def job_edit(request, job_id):
    user = request.user
    profile = Profile.objects.get(user=user)

    job = get_object_or_404(Job, id=job_id)

    if request.method == "POST":
        # import ipdb; ipdb.set_trace()
        form = JobForm(request.POST, instance=job)  # Bind the job instance to the form
        if form.is_valid():
            form.save()
            return redirect('job_list')  # Redirect to the job list after saving the edited job
    else:
        form = JobForm(instance=job)  # Pre-fill the form with job data when editing

    return render(request, "jobs/job_create.html", {
        "form": form, 
        "edit_mode": True,  # Indicate it's an edit operation
        "profile": profile
    })


@login_required
def job_delete(request, job_id):

    return redirect(request, 'jobs/job_list.html')       