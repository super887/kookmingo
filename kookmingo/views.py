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
            'text':today_date +  week_of_day + '요일 의 ' + cafeteria_name +' 메뉴입니다.\n\n'+get_menu(cafeteria_name,week_of_day)
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

    html2= urlopen('http://kmucoop.kookmin.ac.kr/restaurant/restaurant.php?w=3')
    source2 = html2.read()
    html2.close()

    soup2 = BeautifulSoup(source2,"lxml")

    table = soup.find_all("td", class_="ft_mn")
    table2 = soup2.find_all("td", class_="ft_mn")
    i = 0
    j = 0
    for tt in table:
        str = table[i].get_text()
        newstr = str.replace("\n",'')
        int = newstr.find('￦')
        front = newstr[0:int]
        back = newstr[int:-1]
        tt[i] = front + '\n' +back +'0'
        Menu.objects.create(
            cafe_name = 'dd',
            time = 'dd',
            menu = tt[i]
        )
        i=i+1

    for tt in table2:
        str = table2[j].get_text()
        newstr = str.replace("\n",'')
        int = newstr.find('￦')
        front = newstr[0:int]
        back = newstr[int:-1]
        tt[j] = front + '\n' +back +'0'
        Menu.objects.create(
            cafe_name = 'dd',
            time = 'dd',
            menu = tt[j]
        )
        j=j+1

def get_menu(cafeteria_name,week_of_day):
    if week_of_day == '월':
        if cafeteria_name == '복지관(학식)':
            menu = Menu.objects.all()
            a1 = '착한아침--------------------------------\n'+menu[0].menu + '\n\n\n'
            a2 = '중식 가마-------------------------------\n'+menu[7].menu + '\n\n\n'
            a3 = '중식 누들송 면---------------------------\n'+menu[14].menu + '\n\n\n'
            a4 = '중식 누들송 카페테리아------------------\n'+menu[21].menu + '\n\n\n'
            a5 = '중식 인터쉐프----------------------------\n'+menu[28].menu + '\n\n\n'
            a6 = '중식 데일리밥----------------------------\n'+menu[35].menu + '\n\n\n'
            a7 = '석식 가마-------------------------------\n'+menu[42].menu + '\n\n\n'
            a8 = '석식 인터쉐프----------------------------\n'+menu[49].menu + '\n\n\n'
            a9 = '석식 데일리밥----------------------------\n'+menu[56].menu + '\n\n\n'
            a10 = '차이웨이 상시---------------------------\n'+menu[63].menu + '\n\n\n'
            a11 = '차이웨이 특화---------------------------\n'+menu[70].menu
            return a1 + a2 + a3 + a4 + a5+ a6+a7+a8+a9+a10+a11

        elif cafeteria_name == '복지관(교직원)':
            menu = Menu.objects.all()
            b1 = '키친1--------------------------------\n'+menu[0].menu + '\n\n\n'
            b2 = '키친2-------------------------------\n'+menu[7].menu + '\n\n\n'
            b3 = '셀러드바---------------------------\n'+menu[14].menu + '\n\n\n'
            b4 = '석식------------------\n'+menu[21].menu
            return b1 + b2 + b3 + b4


