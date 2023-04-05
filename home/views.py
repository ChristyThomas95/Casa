from django.shortcuts import render, redirect

from store.models import Design
from . models import Teams
from django.contrib import messages

# Create your views here.
def home(request):
    teams = Teams.objects.all()
    featured_design = Design.objects.order_by('-created_at').filter(is_featured=True) 
    all_designs = Design.objects.order_by('-created_at')
    
    
    model_search = Design.objects.values_list('model', flat=True).distinct()
    city_search = Design.objects.values_list('city', flat=True).distinct()
    floors_search = Design.objects.values_list('floors', flat=True).distinct()
    
   
    
    
    context = {
        'teams': teams,
        'featured_design':featured_design,
        'all_designs':all_designs,
        'model_search':model_search,
        'city_search':city_search,
        'floors_search':floors_search,
        
    }
    return render(request, 'home.html',context)



def about(request):
    teams = Teams.objects.all()
    context = {
        'teams': teams
    }
    return render(request, 'pages/about.html', context)



def services(request):
    return render(request, 'pages/services.html')


def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        phone = request.POST['phone']
        message = request.POST['message']
        
        messages.success(request, 'Thank You for contacting us. We will get back to you soon')
        return redirect('contact')
    
    return render(request, 'pages/contact.html')