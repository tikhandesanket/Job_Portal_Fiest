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
        dummy_jobs = [
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
            {
                'title': 'Technical Manager',
                'description': 'Lead technical team projects and ensure timely delivery.',
                'salary': '15,00,000',
                'location': 'Pune, India'
            },
            {
                'title': 'Frontend Developer',
                'description': 'Create responsive and user-friendly web designs.',
                'salary': '7,00,000',
                'location': 'Remote'
            },
            {
                'title': 'Backend Developer',
                'description': 'Build robust backend APIs and manage databases.',
                'salary': '9,00,000',
                'location': 'Hyderabad, India'
            },
            {
                'title': 'DevOps Engineer',
                'description': 'Automate deployments and server management.',
                'salary': '11,00,000',
                'location': 'Chennai, India'
            },
            {
                'title': 'UI/UX Designer',
                'description': 'Design user interfaces for web and mobile apps.',
                'salary': '6,50,000',
                'location': 'Mumbai, India'
            },
            {
                'title': 'Mobile App Developer',
                'description': 'Build and maintain Android/iOS mobile apps.',
                'salary': '8,50,000',
                'location': 'Remote'
            },
            {
                'title': 'Data Scientist',
                'description': 'Analyze data and build predictive models.',
                'salary': '12,00,000',
                'location': 'Bangalore, India'
            },
            {
                'title': 'Project Coordinator',
                'description': 'Coordinate between teams and ensure smooth project execution.',
                'salary': '7,50,000',
                'location': 'Delhi, India'
            },
        ]

    if query:
        dummy_jobs = [job for job in dummy_jobs if query.lower() in job['title'].lower()]
    return render(request, 'jobs/job_list.html', {'jobs': dummy_jobs, 'query': query})

@login_required
def job_create(request):
    return render(request, 'jobs/job_create.html')  # Later form handling here\
 

@login_required
def job_apply(request, job_id):
    # Fetch the job that the user wants to apply for
    # job = get_object_or_404(Job, id=job_id)
    
    # Handle the logic for job application (e.g., saving the application, sending an email, etc.)
    # For now, we just display a confirmation message

    return render(request, 'jobs/job_apply.html', {'job': "job"})        
