# ~/ch/jere-t/django/merchex/listings/views.py

"""Views for listings"""

from django.http import HttpResponse
from django.shortcuts import render


def hello(request):
    """Show view Hello : get HttpRequest and provide a HttpResponse"""
    return HttpResponse('<h1>Hello Django!</h1>')


def about(request):
    """Show view about-us : get HttpRequest and provide a HttpResponse"""
    return HttpResponse('<h1>About us</h1> <p> We love merch !</p>')


def contact(request):
    """Show view contact-us : get HttpRequest and provide a HttpResponse"""
    return HttpResponse(
        '<h1>Contact us</h1> <p> You can contact us by email :  '
        '<a href = "mailto: abc@example.com?subject = Contact Merchex&body ='
        ' Hello...">Send Email</a></p>')


def listings(request):
    """Show view listings : get HttpRequest and provide a HttpResponse"""
    return HttpResponse(
        '<h1>Merch Listings</h1> <p> We have nothing for the moment, '
        'come back later !</p>')
