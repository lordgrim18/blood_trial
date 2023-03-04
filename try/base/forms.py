from django.forms import ModelForm
from .models import Donor,Patient

class DonorForm(ModelForm):
    class Meta:
        model = Donor
        fields = '__all__'

        exclude = ['donor_register',]

#check forms to see if display is possible

class PatientForm(ModelForm):
    class Meta:
        model = Patient
        fields = '__all__'

        exclude = ['patient_register',]