from django.shortcuts import render
from django.http import JsonResponse

def keyboard(request):
    return JsonResponse({
        'type':'buttons',
        'buttons':['학식','법식']
    })
# Create your views here.
