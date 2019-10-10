from django.shortcuts import render, redirect
from django.http import HttpResponse
from lib.crowdScript import CrowdNumber 
from main.models import Hospital
from main.forms import UserInputForm
from lib.combine import Combine
# Create your views here.

def index(request):
    if request.method == 'POST':
        crowdInHospital = CrowdNumber()
        # print(crowdInHospital)
        for hospital in Hospital.objects.all():
            hospital.crowd = crowdInHospital
            hospital.save()

        form = UserInputForm(request.POST)

        result, distance = Combine(form['department_needed'].value(),form['hospital_type'].value())
        # print(result)

        hospital = Hospital.objects.get(pk=result)
        # print(hospital.name)
        # index = form['department_needed'].value()
        # dpt = form['department_needed'][index]
        context = {
            "inputForm": form,
            "hospital": hospital,
            "distance": distance
        }
        return render(request, 'main/details.html', context)
    else:
        form = UserInputForm()
        context = {
            "inputForm": form
        }
        return render(request, 'main/index.html', context)


# def details(request):
#     crowdInHospital = CrowdNumber()
#     for hospital in Hospital.objects.all():
#         hospital.crowd = crowdInHospital
#         hospital.save()
    
#     result = Combine(form.department_needed, form.hospital_type)
#     # if request.method == 'POST':
#     #     form = UserInputForm(request.POST)
#     #     form.save()
#     #     result = Combine(form.department_needed, form.hospital_type)
#     #     hosp = Hospital.objects.get(id = result+1)
#     # else:
#     #     form = UserInputForm()
    

#     # context = {
#     #    'hospital' : hosp 
#     # }
#     return render(request, 'main/details.html')


