from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import  Job, Freelancer
from .forms import FreelancerForm, EmployerForm, MessageForm, JobForm, Level, LoginAsFreelancerForm

# Create your views here.
freelancers = [
    {"id":1, "name": "John"},
    {"id":2, "name": "Abebe"},
    {"id":3, "name":"Alemu"}
]
def homepage(request):
    return render(request, "base/homepage.html")
def home(request):
    jobs = Job.objects.all()
    context = {"jobs":jobs}
    return render(request, "base/home.html", context)
def freelancer(request, pk):
    freelancer = None
    for i in freelancers:
        if i["id"] == int(pk):
           freelancer = i
    context = {"freelancer": freelancer}
    return render(request, 'base/freelancer.html', context)
def signup(request):
    form = FreelancerForm()
    if request.method == "POST":
        form = FreelancerForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect('home')
    context = {"form":form}
    return render(request, 'base/signup.html', context)
def logout(request):
    context = {}
    return render(request, 'base/logout.html', context)
def login(request):
    form = FreelancerForm()
    context = {"form":form}
    return render(request, 'base/login.html', context)
# def loginasfreelancer(request):
#     form = LoginAsFreelancerForm()
#     freelancers = Freelancer.objects.all()
#     jobs = Job.objects.all()
#     if request.method == 'POST':
#         form = LoginAsFreelancerForm(request.POST)
#         if form.is_valid:
#             form.save()
#             return redirect('freelancerpage')
#     context = {"form":form,"jobs":jobs, "freelancers":freelancers}
#     return render(request, 'base/loginasuser.html', context)
def loginasemployer(request):
    form = EmployerForm()
    context = {"form":form}
    return render(request, 'base/login.html', context)
def send_message(request):
    form = MessageForm()
    context = {"form":form}
    return render(request, 'base/send_message.html', context)
def post_job(request):
    form = JobForm()
    if request.method == 'POST':
        form = JobForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {'form': form}
    return render(request, 'base/post_job.html', context)
def apply_job(request):
    context = {}
    return render(request, 'base/proposal.html', context)

def update_job(request, pk):
    job  = Job.objects.get(id=pk)
    form = JobForm(instance=job) 

    if request.method == 'POST':
        form = JobForm(request.POST, instance = job)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form': form}
    return render(request, 'base/update_job.html', context)


def delete_job(request, pk):
    job = Job.objects.get(id = pk)
    if request.method == 'POST':
        job.delete()
        return redirect('home')
    return render(request, 'base/delete_job.html', {'obj':job})

def level(request):
    form = LevelForm()
    if request.method == 'POST':
        form = LevelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {"form": form}
    return render(request, 'base/level.html', context)