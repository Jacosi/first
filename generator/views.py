from django.shortcuts import render
import random

# Create your views here.

def home(request):
    return render(request, 'generator/home.html')


def password(request):
    helper = 'abcdefghijklmnopqrstuvwxyz'
    characters = list(helper)

    length = int(request.GET.get('length'))

    if( request.GET.get('uppercase') ):
        helper = helper.upper()
        characters.extend(list(helper))
    
    if( request.GET.get('numbers') ):
        characters.extend(list('1234567890'))

    if( request.GET.get('special') ):
        characters.extend(list('!@#$%^&*'))


    thepassword = ''
    for _ in range(length):
        thepassword += random.choice(characters) 

    return render(request, 'generator/password.html', {'password': thepassword})