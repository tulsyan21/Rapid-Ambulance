from django.shortcuts import render
from django.http import HttpResponse
from lib.crowdScript import CrowdNumber 
from main.models import Hospital
# Create your views here.

def index(request):
    return render(request, 'main/index.html')

def details(request):
    crowdInHospital = CrowdNumber()
    print(crowdInHospital)
    for hospital in Hospital.objects.all():
        hospital.crowd = crowdInHospital
        hospital.save()

    return render(request, 'main/details.html')
