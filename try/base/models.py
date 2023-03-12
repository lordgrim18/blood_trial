from django.db import models
from django.contrib.auth.models import User

# Create your models here.

#donate
class Donor(models.Model):
    donor_register = models.ForeignKey(User, on_delete=models.CASCADE) #check if this is necessary -- used to make many to one relationship
    name = models.CharField(max_length=200)
    blood_group = models.CharField(max_length=10)
    DOB = models.DateField()
    mobile_no = models.BigIntegerField(unique=True)   #enter restrictions so tht phone number is 10 digit  
    state = models.CharField(max_length=200)
    district = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    email_id = models.EmailField()
    availability = models.BooleanField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-updated', '-created']     #updation or deletion probably require.....remember to check

    def __str__(self):
        return self.name


class Patient(models.Model):
    patient_register = models.ForeignKey(User, on_delete=models.CASCADE)
    patient_name = models.CharField(max_length=200)
    bystander_name = models.CharField(max_length=200)
    blood_group = models.CharField(max_length=10)
    required_date = models.DateField()
    admitted_hospital = models.CharField(max_length=200)
    bystander_no = models.BigIntegerField()
    place = models.CharField(max_length=200)
    district = models.CharField(max_length=200)
    units = models.SmallIntegerField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-updated','-created']

    def __str__(self):
        return self.patient_name
