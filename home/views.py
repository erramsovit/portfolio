from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'home.html',context={'home':'active'})

def services(request):
    return render(request,'services.html',context={'services':'active'})

def skills(request):
     return render(request,'skills.html',context={'skills':'active'})

def contact(request):
     return render(request,'contact.html',context={'contact':'active'})



