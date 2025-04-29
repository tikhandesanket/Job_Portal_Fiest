from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Job

@login_required
def job_list(request):
    # If you have real Job records, use this:
    jobs = Job.objects.all()
    query = request.GET.get('q', '')
    # If you don't have real records yet, use dummy data temporarily:
    if not jobs.exists():
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
    jobsList = jobs   

    if query:
        jobsList = [job for job in jobs if query.lower() in job['title'].lower()]
    return render(request, 'jobs/job_list.html', {'jobs': jobsList, 'query': query})

from django.shortcuts import render, redirect

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
