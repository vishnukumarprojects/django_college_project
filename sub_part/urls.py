from django.urls import path
from . import views


urlpatterns=[
    path('',views.index,name='index'),
    path('tata',views.tata,name='tata'),
    path('book_now',views.book_now,name='book_now'),
    path('bmw',views.bmw,name='bmw'),
    path('mahindra',views.mahindra,name='mahindra'),
    path('maruthi',views.maruthi,name='maruthi'),
    path('toyato',views.toyato,name='toyato'),
    path('kia',views.kia,name='kia'),
    path('benz',views.benz,name='benz'),
    path('renault',views.renault,name='renault'),
    path('audi',views.audi,name='audi'),
    path('volkswagen',views.volkswagen,name='volkswagen'),
    path('companys',views.companys,name='companys'),
    path('contact',views.contact,name='contact'),
    path('profile',views.profile,name='profile'),
    path('user_profile',views.user_profile,name='user_profile'),
    path('terms_and_conditions',views.terms_and_conditions,name='terms_and_conditions'),
    path('privacy_policy',views.privacy_policy,name='privacy_policy'),
    path('aboutus',views.aboutus,name='aboutus'),
    path('cancel_booking', views.cancel_booking, name='cancel_booking'),
    path('cancelled_intimation', views.cancelled_intimation, name='cancelled_intimation'),
    
]


