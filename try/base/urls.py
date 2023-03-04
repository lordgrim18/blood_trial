from django.urls import path
from . import views


urlpatterns = [
    path('',views.home, name="home"),

    path('login/',views.loginPage, name='login'),
    path('logout/',views.logoutUser, name='logout'),
    path('register/',views.registerPage, name='register'),

    path('profile/<str:pk>',views.userProfile, name='profile'),

    path('donor/<str:pk>/',views.donate, name='view-donate'),
    path('create-donor/',views.createDonate, name='create-donate'),
    path('update-donor/<str:pk>/',views.updateDonate, name='update-donate'),
    path('delete-donor/<str:pk>/',views.deleteDonate, name='delete-donate'),

    path('patient/<str:pk>/',views.patient, name='view-patient'),
    path('create-patient/',views.addPatient, name='create-patient'),
    path('update-patient/<str:pk>/',views.updatePatient, name='update-patient'),
    path('delete-patient/<str:pk>/',views.deletePatient, name='delete-patient'),

    path('donors-list/',views.donorsList, name='donors-list'),
    path('patients-list/',views.patientsList, name='patients-list'),

    path('find-donor/',views.find_donor, name='find-donor'),

    path('about/',views.aboutPage, name='about'),
    path('contact/',views.contactPage, name='contact'),


]