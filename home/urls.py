from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path("",views.index, name = 'index'),
    path("login", views.login, name = 'login'),
    path("main", views.main, name = 'main'),
    path('heart',views.heart,name='heart'),
    path('diabetes',views.diabetes,name='diabetes'),
    path("covid-checker",views.covid, name = 'covid'),
    path("hospital-locator",views.hospital, name = 'hospital'),
    path("pharmacy-locator",views.pharmacy, name = 'pharmacy'),
    path("medstore",views.medstore, name = 'medstore'),
    path("checkout",views.checkout, name = 'checkout'),
    path("confirmation-page",views.confirmation, name = 'confirmation'),
    path("forgot-pass",views.forgot, name = 'forgot'),
    path("mobile-app",views.mobile, name = 'mobile'),
    path("faq",views.faq, name = 'faq'),
    path("about",views.about, name = 'about'),
    path("contact",views.contact, name = 'contact'),
    # path("",views.index, name = 'index'),
    # path("",views.index, name = 'index'),
    # path("",views.index, name = 'index'),

]
