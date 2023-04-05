from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Contact
# Create your views here.

def inquiry(request):
    if request.method == 'POST':
        design_id = request.POST['design_id']
        design_title = request.POST['design_title']
        user_id = request.POST['user_id']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        customer_need = request.POST['customer_need']
        city = request.POST['city']
        province = request.POST['province']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        
        contact = Contact(design_id=design_id, design_title=design_title, user_id=user_id, 
        first_name=first_name, last_name=last_name, customer_need=customer_need, city=city, province=province, email=email, phone=phone, message=message)
        
        contact.save()
        messages.success(request, 'Your request has been submitted, we will get back to you shortly')
                
        return redirect('home') 