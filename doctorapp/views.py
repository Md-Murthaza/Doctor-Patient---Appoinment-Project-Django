from django.shortcuts import render
from .models import Doctor
# Create your views here.

def base_view(request):
    return render(request,'Base.html')




def doctor_list(request):
    doctors = Doctor.objects.all()
    return render(request,'doctor_list.html',{'doctors':doctors})
