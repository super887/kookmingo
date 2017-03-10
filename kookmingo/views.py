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

    return JsonResponse({
        'message':{
            'text':today_date + ' 의 ' + cafeteria_name +'중식 메뉴입니다.\n \n'+ get_menu(cafeteria_name)
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
    Menu.menu = table[0]
    return create_menu_db('복지관','11',Menu.menu)


def create_menu_db(cafe_name,time,menu):
    Menu.objects.create(
        cafe_name = cafe_name,
        time = time,
        menu = menu,
    )

def get_menu(cafeteria_name):
    if cafeteria_name == '복지관(학식)':
        sang1 = Menu.objects.get(cafe_name='백반코너').menu
        sang2 = Menu.objects.get(cafe_name='일품코너').menu

        return "----------\n" + "백반코너\n" +sang1 \
                +"----------\n" + "일품코너\n" +sang2\
# Create your views here.
