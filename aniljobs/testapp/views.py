from django.shortcuts import render


# Create your views here.
def home_page_view(request):
    return render(request,'testapp/index.html')
from testapp.models import HydJobs
def hyd_jobs_view(request):
    jobs_list = HydJobs.objects.all()
    return render(request,'testapp/hydjobs.html',{'jobs_list':jobs_list})
from testapp.models import PuneJobs
def pune_jobs_view(request):
    jobs_list = PuneJobs.objects.all()
    return render(request,'testapp/punejobs.html',{'jobs_list':jobs_list})
from testapp.models import BangaloreJobs
def bangalore_jobs_view(request):
    jobs_list = BangaloreJobs.objects.all()
    return render(request,'testapp/bangalorejobs.html',{'jobs_list':jobs_list})