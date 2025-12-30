from django.db import models





# Create your models here.



class customer_register_table(models.Model):
    car_model=models.CharField(max_length=50)
    days=models.CharField(max_length=50)
    pickup_date=models.CharField(max_length=50)
    drop_date=models.CharField(max_length=100)
    full_name=models.CharField(max_length=100)
    father_name=models.CharField(max_length=100)
    mother_name=models.CharField(max_length=100)
    gender=models.CharField(max_length=10)
    dob=models.CharField(max_length=50)
    state=models.CharField(max_length=100)
    district=models.CharField(max_length=100)
    pincode=models.CharField(max_length=6)
    current_address=models.CharField(max_length=500)
    permanent_address=models.CharField(max_length=500)
    phone_number=models.CharField(max_length=10)
    booking_number=models.CharField(max_length=50)
    email_id = models.EmailField()
    alternative_number=models.CharField(max_length=10)
    aadhar_number=models.CharField(max_length=50)
    licence_type=models.CharField(max_length=20)
    licence_number=models.CharField(max_length=50)


class customer_review(models.Model):
    review=models.CharField(max_length=1000)
    booking_number=models.CharField(max_length=30)
    email_id=models.CharField(max_length=50)

class cancellation(models.Model):
    booking_number=models.CharField(max_length=50)
    email_id=models.EmailField()
    





    
     

