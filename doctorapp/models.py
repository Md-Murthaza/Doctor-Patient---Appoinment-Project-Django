from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.

class Doctor(models.Model):
    user = models.OneToOneField(User,on_delete = models.CASCADE)
    specialty = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=100)
    office_address = models.CharField(max_length=300)




    def __str__(self):
        return f"Dr. {self.user.username} - {self.specialty}"


class Patient(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    date_of_birth = models.DateField()
    phone_number = models.CharField(max_length=100)



    def __str__(self):
        return f"{self.user.username} - {self.date_of_birth}"



class Appoinment(models.Model):
    STATUS_CHOICES = [
        ('Pending','Pending'),
        ('Confirmed' , 'Confirmed'),
        ('Cancelled','Cancelled'),
        ('Completed','Completed'),

    ]


    patient = models.ForeignKey(Patient,on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor,on_delete=models.CASCADE)
    appoinments_time = models.DateTimeField()
    status = models.CharField(max_length=10,choices=STATUS_CHOICES,default='Pending')
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return f"Appoinment {self.id} - {self.patient.user.username} with Dr. {self.doctor.user.username} on {self.appoinments_time}"

    
    def is_past_due(self):
        return self.appoinments_time < timezone.now() and self.status != 'Completed'

    



    



