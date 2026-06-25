from django.shortcuts import render
from . models import *
from django.contrib import messages
# ---------mailsenderlibrary----------
from django.core.mail import send_mail
from django.conf import settings
# -------------------------------------
import random

# from twilio.rest import Client


# Create your views here.

    



def index(request):
    return render(request,'index.html')

def tata(request):
    return render(request,'tata.html')

def bmw(request):
    return render(request,'bmw.html')

def mahindra(request):
    return render(request,'mahindra.html')

def maruthi(request):
    return render(request,'maruthi.html')

def toyato(request):
    return render(request,'toyato.html')

def kia(request):
    return render(request,'kia.html')

def benz(request):
    return render(request,'benz.html')

def renault(request):
    return render(request,'renault.html')


def audi(request):
   
    return render(request,'audi.html')

def volkswagen(request):
    return render(request,'volkswagen.html')

def companys(request):
    return render(request,'companys.html')

def contact(request):
    return render(request,'contact.html')

def user_profile(request):
    if request.method=="POST":
        review=request.POST.get('review')
        booking_number = request.POST.get('booking_number') 
        email_id= request.POST.get('email_id') 
        ex6=customer_review(review=review,booking_number=booking_number,email_id=email_id)
        ex6.save()
        messages.success(request,review, extra_tags='success')
        return render(request,'user_profile.html')
    
        
    return render(request, 'user_profile.html')

def cancel_booking(request):
    if request.method=="POST":
        booking_number=request.POST.get('booking_number')
        email_id=request.POST.get('email_id')
        
        ex2=cancellation(booking_number=booking_number,email_id=email_id)
        ex2.save()
        return render(request,'cancelled_intimation.html')
    return render(request,'cancel_booking.html')
    
    
        
    
        


def cancelled_intimation(request):
    return render(request,'cancelled_intimation.html')

  
    
    
    
        
        
       

def terms_and_conditions(request):
    return render(request,'terms_and_conditions.html')

def privacy_policy(request):
    return render(request,'privacy_policy.html')

def aboutus(request):
    return render(request,'aboutus.html')
    
def profile(request):
    if request.method=="POST":
        if customer_register_table.objects.filter(booking_number=request.POST.get('booking_number'),email_id=request.POST.get('email_id')):
            logger_data=customer_register_table.objects.get(booking_number=request.POST.get('booking_number'),email_id=request.POST.get('email_id'))
            return render(request,'user_profile.html',{'logger_data':logger_data})
        else:
            messages.error(request,'Username or Password invalid',extra_tags='failed')
            return render(request,'profile.html')
    else:
        return render(request,'profile.html')

def book_now(request):
    if request.method=="POST":
        days=request.POST.get('days')
        pickup_date=request.POST.get('pickup_date')
        drop_date=request.POST.get('drop_date')
        full_name=request.POST.get('full_name')
        father_name=request.POST.get('father_name')
        mother_name=request.POST.get('mother_name')
        licence_type=request.POST.get('licence_type')
        gender=request.POST.get('gender')
        car_model=request.POST.get("car_model")
        dob=request.POST.get('dob')
        state=request.POST.get('state')
        district=request.POST.get('district')
        pincode=request.POST.get('pincode')
        current_address=request.POST.get('current_address')
        permanent_address=request.POST.get('permanent_address')
        phone_number=request.POST.get('phone_number')
        email_id=request.POST.get('email_id')
        alternative_number=request.POST.get('alternative_number')
        licence_number=request.POST.get('licence_number')
        aadhar_number=request.POST.get('aadhar_number')
        random_number=random.randint(00000,99999)
        company_code="GSDCARS2025TN23"
        booking_number=company_code+str(random_number)

        ex1=customer_register_table(full_name=full_name,
        father_name=father_name,
        mother_name=mother_name,
        state=state,district=district,
        pincode=pincode,
        current_address=current_address,
        permanent_address=permanent_address,
        alternative_number=alternative_number,
        email_id=email_id,
        phone_number=phone_number,
        licence_number=licence_number,
        licence_type=licence_type,
        gender=gender,
        dob=dob,
        car_model=car_model,
        pickup_date=pickup_date,
        drop_date=drop_date,
        aadhar_number=aadhar_number,
        days=days,
        booking_number=booking_number
            )

        ex1.save()
            
        #Mail send logic
        try:
            subject='GSDCars Booked successfully'
            message=f'Hi  {full_name}  Your Car Booking Number:{booking_number} GSDCars Model:  {car_model}  for {days} was Booked Successfully.\n Your Car Pickup Date  {pickup_date},\n The Time has considered by when the car pickup time for  {days}  as drop date:{drop_date}..'
            send_mail(subject, message, settings.EMAIL_HOST_USER, [email_id])
            print('Email sent successfully')
        except Exception as e:
            print('Email no sent')
        return render(request,'profile.html')
            
       
    else:
        return render(request,'book_now.html')


   




