from django.shortcuts import render
from django.http import JsonResponse
import json, datetime
from django.views.decorators.csrf import csrf_exempt

def keyboard(request):
    return JsonResponse(
        {
        'type':'buttons',
        'buttons':['상록','그루터기']
    })

@csrf_exempt
def answer(request):
    json_str = ((request.body).decode('utf-8'))
    received_json_data = json.loads(json_str)
    cafeteria_name = received_json_data['content']
    today_date = datetime.date.today().strftime("%m월 %d일")

    return JsonResponse({
        'message':{
            'text':today_date + 'of' + cafeteria_name +'middle'
        },
        'keyboard':{
            'type':'buttons',
            'buttons':['상록','그루터기']
        }
    })

# Create your views here.
