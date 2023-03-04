from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q      #allows us to use & and | by using Q
from django.contrib.auth.models import User 
from django.contrib.auth import authenticate,login , logout
from django.contrib.auth.forms import UserCreationForm
from .models import Donor, Patient
from .forms import DonorForm, PatientForm
from .filters import OrderFilter

# Create your views here.
#remember to addd all error messages like error 404

def home(request):
    donors = Donor.objects.all()
    donors_count = donors.count()
    patients = Patient.objects.all()
    patients_count = patients.count()
    context = {'donors': donors, 'donors_count': donors_count,'patients': patients, 'patients_count': patients_count}
    return render(request, 'base/home.html', context)

def donorsList(request):
    donors = Donor.objects.all()
    context = {'donors': donors}
    return render(request, 'base/donors_list.html', context)

def patientsList(request):
    patients = Patient.objects.all()
    context = {'patient': patient}
    return render(request, 'base/patients_list.html',context)


def loginPage(request):
    page = 'login'

    if request.user.is_authenticated:
        return redirect('home')
    
    if request.method == 'POST':
        username = request.POST.get('username').lower()
        password = request.POST.get('password')
        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'User does not exist')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')     #instead of home go back to the previous page???
        else:
            messages.error(request, 'Incorrect password')

    context = {'page':page}
    return render(request, 'base/login_register.html', context)



def registerPage(request):
    form = UserCreationForm()

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'An error has occured')

    return render(request, 'base/login_register.html', {'form': form})

def logoutUser(request):
    logout(request)
    return redirect('home')


@login_required(login_url='login')
def userProfile(request,pk):
    user = User.objects.get(id=pk)
    donors = user.donor_set.all()
    patients = user.patient_set.all()

    context = {'user':user, 'donors':donors, 'patients': patients}
    return render(request, 'base/profile.html', context)



@login_required(login_url='login')
def donate(request,pk):
    donor = Donor.objects.get(id=pk)    


    context = {'donor': donor}
    return render(request, 'base/donor.html', context)

@login_required(login_url='login')
def createDonate(request):
    form = DonorForm()
    if request.method == 'POST':
        form = DonorForm(request.POST)
        if form.is_valid():
            donor = form.save(commit=False)
            donor.donor_register = request.user
            donor.save()
            return redirect('home')     #change from home to the donor page 

    context = {'form': form}
    return render(request, 'base/donor_form.html', context)

@login_required(login_url='login')
def updateDonate(request,pk):
    donor = Donor.objects.get(id=pk)
    form = DonorForm(instance=donor)

    if request.user != donor.donor_register:
        return HttpResponse("you arent allowed here!!!")

    if request.method == 'POST':
        form = DonorForm(request.POST, instance=donor)
        if form.is_valid():
            form.save()
            return redirect('home')     #cahnge destination to donor page???

    context = {'form': form}
    return render(request, 'base/donor_form.html', context)

@login_required(login_url='login')
def deleteDonate(request,pk):
    donor = Donor.objects.get(id=pk)

    if request.user != donor.donor_register:
        return HttpResponse("you arent allowed here!!!!!!")
    if request.method == 'POST':
        donor.delete()
        return redirect('home')
    
    context = {'donor': donor}
    return render(request, 'base/delete.html', context)


@login_required(login_url='login')
def patient(request,pk):
    patient = Patient.objects.get(id=pk)

    context = {'patient': patient}
    return render(request, 'base/patient.html', context)

@login_required(login_url='login')
def addPatient(request):
    form = PatientForm()
    if request.method == 'POST':
        form = PatientForm(request.POST)
        if form.is_valid():
            patient = form.save(commit=False)
            patient.patient_register = request.user
            patient.save()
            return redirect('home')     #change from home to the patient page or to the search page

    context = {'form': form}
    return render(request, 'base/patient_form.html', context)



@login_required(login_url='login')
def updatePatient(request,pk):
    patient = Patient.objects.get(id=pk)
    form = PatientForm(instance=patient)
    if request.user != patient.patient_register:
        return HttpResponse("you arent allowed here!!!")

    if request.method == 'POST':
        form = PatientForm(request.POST,instance=patient)
        if form.is_valid():
            form.save()
            return redirect('home')     #cahnge to home to patient??

    context = {'form': form}
    return render(request, 'base/patient_form.html', context)


@login_required(login_url='login')
def deletePatient(request,pk):
    patient = Patient.objects.get(id=pk)

    if request.user != patient.patient_register:
        return HttpResponse("you arent allowed here!!!")

    if request.method == 'POST':
        patient.delete()
        return redirect('home')
     
    context = {'patient': patient}
    return render(request, 'base/delete.html', context)

    


@login_required(login_url='login')
def find_donor(request):
    
    donors = Donor.objects.all()
    
    myFilter = OrderFilter(request.GET, queryset=donors)
    donors = myFilter.qs 
    donors_count = donors.count()

    context = {'donors': donors,'donors_count': donors_count, 'myFilter': myFilter}
    return render(request, 'base/find_donor.html', context)

def aboutPage(request):
    return render(request, 'base/about.html')

def contactPage(request):
    return render(request, 'base/contact.html')


