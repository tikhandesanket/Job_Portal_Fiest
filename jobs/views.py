from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import Job

@login_required
def job_list(request):
    query = request.GET.get('q', '')

    jobs_qs = Job.objects.filter(posted_by=request.user)
    using_dummy_data = not jobs_qs.exists()

    if using_dummy_data:
        jobs = [
            {
                'title': 'Software Developer',
                'description': 'Develop and maintain software applications.',
                'salary': '8,00,000',
                'location': 'Mumbai, India'
            },
            {
                'title': 'Full Stack Developer',
                'description': 'Work on frontend and backend systems.',
                'salary': '10,00,000',
                'location': 'Bangalore, India'
            },
        ]
        if query:
            jobsList = [job for job in jobs if query.lower() in job['title'].lower()]
        else:
            jobsList = jobs
    else:
        if query:
            jobsList = jobs_qs.filter(title__icontains=query)
        else:
            jobsList = jobs_qs

    return render(request, 'jobs/job_list.html', {'jobs': jobsList, 'query': query})


@login_required
def job_create(request):
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

    return render(request, 'jobs/job_create.html')



@login_required
def job_apply(request, job_id):

    return render(request, 'jobs/job_apply.html', {'job': "job"})        
