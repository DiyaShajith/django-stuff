from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render

def print_hello(request):
    context={
        'title':'Godfather',
        'year':1990,
        'summary':'story of an underworld king'
    }
    print(context)
    return render(request,'hello.html',context)
    