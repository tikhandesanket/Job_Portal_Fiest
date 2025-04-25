from django.shortcuts import render

def job_list(request):
    jobs = Job.objects.all()
    return render(request, 'jobs/job_list.html', {'jobs': jobs})

def job_create(request):
    return render(request, 'jobs/job_create.html')  # form handling logic
