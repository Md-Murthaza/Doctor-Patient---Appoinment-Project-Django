from django.shortcuts import render
from .models import Doctor
from .forms import AppoinmentForm
from django.utils import timezone
# Create your views here.

def base_view(request):
    return render(request,'Base.html')

def doctor_list(request):
    doctors = Doctor.objects.all()
    return render(request,'doctor_list.html',{'doctors':doctors})


def book_appointment(request):
    if request.method == 'POST':
        form = AppoinmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('appointment success')

    else:
        form = AppoinmentForm()


    return render(request,'book_appointment.html',{'form':form})


def appointment_success(request):
    return render(request,'appoinment_success.html')

