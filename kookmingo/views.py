from django.shortcuts import render
from django.http import JsonResponse
from .models import Menu
import json, datetime
from django.views.decorators.csrf import csrf_exempt
from bs4 import BeautifulSoup
from urllib.request import urlopen

def keyboard(request):
    return JsonResponse(
        {
        'type':'buttons',
        'buttons':['복지관(학식)','복지관(교직원)','법식']
    })

@csrf_exempt
def answer(request):
    json_str = ((request.body).decode('utf-8'))
    received_json_data = json.loads(json_str)
    cafeteria_name = received_json_data['content']
    today_date = datetime.date.today().strftime("%m월 %d일")
    week= ['월','화','수','목','금','토','일']
    week_day = datetime.datetime.today().weekday()
    week_of_day = week[week_day]

    return JsonResponse({
        'message':{
            'text':today_date +  week_of_day + '요일 의 ' + cafeteria_name +' 메뉴입니다.\n'+get_menu(cafeteria_name,week_of_day)
        },
        'keyboard':{
            'type':'buttons',
            'buttons': ['복지관(학식)', '복지관(교직원)', '법식']
        }
    })

def crawl(request):
    menu_db = Menu.objects.all()
    menu_db.delete()

    html= urlopen('http://kmucoop.kookmin.ac.kr/restaurant/restaurant.php?w=2')
    source = html.read()
    html.close()

    soup = BeautifulSoup(source,"lxml")

    table = soup.find_all("td", class_="ft_mn")
    i = 0;
    for tt in table:
        str = table[i].get_text()
        newstr = str.replace("\n",'')
        newnewstr = newstr.replace("￦",'')
        tt[i] = newstr
        Menu.objects.create(
            cafe_name = 'dd',
            time = 'dd',
            menu = tt[i]
        )
        i=i+1

def get_menu(cafeteria_name,week_of_day):
    if week_of_day == '월':
        if cafeteria_name == '복지관(학식)':
            menu = Menu.objects.all()
            a1 = menu[0].menu
            a2 = menu[7].menu
            a3 = menu[14].menu
            a4 = menu[21].menu
            a5 = menu[28].menu
            a6 = menu[35].menu
            a7 = menu[42].menu
            a8 = menu[49].menu
            a9 = menu[56].menu
            a10 = menu[63].menu
            a11 = menu[70].menu
            return a1 + a2 + a3 + a4 + a5+ a6+a7+a8+a9+a10+a11


