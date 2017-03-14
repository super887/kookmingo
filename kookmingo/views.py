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
        'buttons':['복지관(학식)','복지관(교직원)','법식(한울)']
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
            'text':today_date + '('+ week_of_day + '요일) ' + cafeteria_name +' 메뉴\n\n'+get_menu(cafeteria_name,week_of_day)
        },
        'keyboard':{
            'type':'buttons',
            'buttons': ['복지관(학식)', '복지관(교직원)','법식(한울)']
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

    html3= urlopen('http://kmucoop.kookmin.ac.kr/restaurant/restaurant.php?w=1')
    source3 = html3.read()
    html3.close()
    soup3 = BeautifulSoup(source3,"lxml")

    table = soup.find_all("td", class_="ft_mn")
    table2 = soup2.find_all("td", class_="ft_mn")
    table3 = soup3.find_all("td", class_="ft_mn")
    i = 0
    j = 0
    k = 0
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

    for tt in table3:
        str = table3[k].get_text()
        int = newstr.find('￦')
        front = newstr[0:int]
        back = newstr[int:-1]
        tt[k] = front + '\n' +back +'0'
        Menu.objects.create(
            cafe_name = 'dd',
            time = 'dd',
            menu = tt[k]
        )
        k=k+1



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
            b1 = '키친1--------------------------------\n'+menu[77].menu + '\n\n\n'
            b2 = '키친2-------------------------------\n'+menu[84].menu + '\n\n\n'
            b3 = '셀러드바---------------------------\n'+menu[91].menu + '\n\n\n'
            b4 = '석식------------------\n'+menu[98].menu
            return b1 + b2 + b3 + b4

        elif cafeteria_name == '법식(한울)':
            menu = Menu.objects.all()
            c1 = '바로바로---------------------------\n'+menu[105].menu+ '\n\n\n'
            c2 = '바로바로2---------------------------\n'+menu[112].menu+ '\n\n\n'
            c3 = '면이랑---------------------------\n'+menu[119].menu+ '\n\n\n'
            c4 = '밥이랑하나-------------------------\n'+menu[126].menu+ '\n\n\n'
            c5 = '밥이랑두울-------------------------\n'+menu[133].menu+ '\n\n\n'
            c6 = '석쇠랑---------------------------\n'+menu[140].menu+ '\n\n\n'
            c7 = '석쇠랑(조식)-----------------------\n'+menu[147].menu+ '\n\n\n'
            return c1+c2+c3+c4+c5+c6+c7

    elif week_of_day == '화':
        if cafeteria_name == '복지관(학식)':
            menu = Menu.objects.all()
            a1 = '착한아침--------------------------------\n'+menu[1].menu + '\n\n\n'
            a2 = '중식 가마-------------------------------\n'+menu[8].menu + '\n\n\n'
            a3 = '중식 누들송 면---------------------------\n'+menu[15].menu + '\n\n\n'
            a4 = '중식 누들송 카페테리아------------------\n'+menu[22].menu + '\n\n\n'
            a5 = '중식 인터쉐프----------------------------\n'+menu[29].menu + '\n\n\n'
            a6 = '중식 데일리밥----------------------------\n'+menu[36].menu + '\n\n\n'
            a7 = '석식 가마-------------------------------\n'+menu[43].menu + '\n\n\n'
            a8 = '석식 인터쉐프----------------------------\n'+menu[50].menu + '\n\n\n'
            a9 = '석식 데일리밥----------------------------\n'+menu[57].menu + '\n\n\n'
            a10 = '차이웨이 상시---------------------------\n'+menu[64].menu + '\n\n\n'
            a11 = '차이웨이 특화---------------------------\n'+menu[71].menu
            return a1 + a2 + a3 + a4 + a5+ a6+a7+a8+a9+a10+a11

        elif cafeteria_name == '복지관(교직원)':
            menu = Menu.objects.all()
            b1 = '키친1--------------------------------\n'+menu[78].menu + '\n\n\n'
            b2 = '키친2-------------------------------\n'+menu[85].menu + '\n\n\n'
            b3 = '셀러드바---------------------------\n'+menu[92].menu + '\n\n\n'
            b4 = '석식------------------\n'+menu[99].menu
            return b1 + b2 + b3 + b4

        elif cafeteria_name == '법식(한울)':
            menu = Menu.objects.all()
            c1 = '바로바로---------------------------\n'+menu[106].menu+ '\n\n\n'
            c2 = '바로바로2---------------------------\n'+menu[113].menu+ '\n\n\n'
            c3 = '면이랑---------------------------\n'+menu[120].menu+ '\n\n\n'
            c4 = '밥이랑하나-------------------------\n'+menu[127].menu+ '\n\n\n'
            c5 = '밥이랑두울-------------------------\n'+menu[134].menu+ '\n\n\n'
            c6 = '석쇠랑---------------------------\n'+menu[141].menu+ '\n\n\n'
            c7 = '석쇠랑(조식)-----------------------\n'+menu[148].menu+ '\n\n\n'
            return c1+c2+c3+c4+c5+c6+c7
    elif week_of_day == '수':
        if cafeteria_name == '복지관(학식)':
            menu = Menu.objects.all()
            a1 = '착한아침--------------------------------\n'+menu[2].menu + '\n\n\n'
            a2 = '중식 가마-------------------------------\n'+menu[9].menu + '\n\n\n'
            a3 = '중식 누들송 면---------------------------\n'+menu[16].menu + '\n\n\n'
            a4 = '중식 누들송 카페테리아------------------\n'+menu[23].menu + '\n\n\n'
            a5 = '중식 인터쉐프----------------------------\n'+menu[30].menu + '\n\n\n'
            a6 = '중식 데일리밥----------------------------\n'+menu[37].menu + '\n\n\n'
            a7 = '석식 가마-------------------------------\n'+menu[44].menu + '\n\n\n'
            a8 = '석식 인터쉐프----------------------------\n'+menu[51].menu + '\n\n\n'
            a9 = '석식 데일리밥----------------------------\n'+menu[58].menu + '\n\n\n'
            a10 = '차이웨이 상시---------------------------\n'+menu[65].menu + '\n\n\n'
            a11 = '차이웨이 특화---------------------------\n'+menu[72].menu
            return a1 + a2 + a3 + a4 + a5+ a6+a7+a8+a9+a10+a11

        elif cafeteria_name == '복지관(교직원)':
            menu = Menu.objects.all()
            b1 = '키친1--------------------------------\n'+menu[79].menu + '\n\n\n'
            b2 = '키친2-------------------------------\n'+menu[86].menu + '\n\n\n'
            b3 = '셀러드바---------------------------\n'+menu[93].menu + '\n\n\n'
            b4 = '석식------------------\n'+menu[100].menu
            return b1 + b2 + b3 + b4

        elif cafeteria_name == '법식(한울)':
            menu = Menu.objects.all()
            c1 = '바로바로---------------------------\n'+menu[107].menu+ '\n\n\n'
            c2 = '바로바로2---------------------------\n'+menu[114].menu+ '\n\n\n'
            c3 = '면이랑---------------------------\n'+menu[121].menu+ '\n\n\n'
            c4 = '밥이랑하나-------------------------\n'+menu[128].menu+ '\n\n\n'
            c5 = '밥이랑두울-------------------------\n'+menu[135].menu+ '\n\n\n'
            c6 = '석쇠랑---------------------------\n'+menu[142].menu+ '\n\n\n'
            c7 = '석쇠랑(조식)-----------------------\n'+menu[149].menu+ '\n\n\n'
            return c1+c2+c3+c4+c5+c6+c7

    elif week_of_day == '목':
        if cafeteria_name == '복지관(학식)':
            menu = Menu.objects.all()
            a1 = '착한아침--------------------------------\n'+menu[3].menu + '\n\n\n'
            a2 = '중식 가마-------------------------------\n'+menu[10].menu + '\n\n\n'
            a3 = '중식 누들송 면---------------------------\n'+menu[17].menu + '\n\n\n'
            a4 = '중식 누들송 카페테리아------------------\n'+menu[24].menu + '\n\n\n'
            a5 = '중식 인터쉐프----------------------------\n'+menu[31].menu + '\n\n\n'
            a6 = '중식 데일리밥----------------------------\n'+menu[38].menu + '\n\n\n'
            a7 = '석식 가마-------------------------------\n'+menu[45].menu + '\n\n\n'
            a8 = '석식 인터쉐프----------------------------\n'+menu[52].menu + '\n\n\n'
            a9 = '석식 데일리밥----------------------------\n'+menu[59].menu + '\n\n\n'
            a10 = '차이웨이 상시---------------------------\n'+menu[66].menu + '\n\n\n'
            a11 = '차이웨이 특화---------------------------\n'+menu[73].menu
            return a1 + a2 + a3 + a4 + a5+ a6+a7+a8+a9+a10+a11

        elif cafeteria_name == '복지관(교직원)':
            menu = Menu.objects.all()
            b1 = '키친1--------------------------------\n'+menu[80].menu + '\n\n\n'
            b2 = '키친2-------------------------------\n'+menu[87].menu + '\n\n\n'
            b3 = '셀러드바---------------------------\n'+menu[94].menu + '\n\n\n'
            b4 = '석식------------------\n'+menu[101].menu
            return b1 + b2 + b3 + b4

        elif cafeteria_name == '법식(한울)':
            menu = Menu.objects.all()
            c1 = '바로바로---------------------------\n'+menu[108].menu+ '\n\n\n'
            c2 = '바로바로2---------------------------\n'+menu[115].menu+ '\n\n\n'
            c3 = '면이랑---------------------------\n'+menu[122].menu+ '\n\n\n'
            c4 = '밥이랑하나-------------------------\n'+menu[129].menu+ '\n\n\n'
            c5 = '밥이랑두울-------------------------\n'+menu[136].menu+ '\n\n\n'
            c6 = '석쇠랑---------------------------\n'+menu[143].menu+ '\n\n\n'
            c7 = '석쇠랑(조식)-----------------------\n'+menu[150].menu+ '\n\n\n'
            return c1+c2+c3+c4+c5+c6+c7
    elif week_of_day == '금':
        if cafeteria_name == '복지관(학식)':
            menu = Menu.objects.all()
            a1 = '착한아침--------------------------------\n'+menu[4].menu + '\n\n\n'
            a2 = '중식 가마-------------------------------\n'+menu[11].menu + '\n\n\n'
            a3 = '중식 누들송 면---------------------------\n'+menu[18].menu + '\n\n\n'
            a4 = '중식 누들송 카페테리아------------------\n'+menu[25].menu + '\n\n\n'
            a5 = '중식 인터쉐프----------------------------\n'+menu[32].menu + '\n\n\n'
            a6 = '중식 데일리밥----------------------------\n'+menu[39].menu + '\n\n\n'
            a7 = '석식 가마-------------------------------\n'+menu[46].menu + '\n\n\n'
            a8 = '석식 인터쉐프----------------------------\n'+menu[53].menu + '\n\n\n'
            a9 = '석식 데일리밥----------------------------\n'+menu[60].menu + '\n\n\n'
            a10 = '차이웨이 상시---------------------------\n'+menu[67].menu + '\n\n\n'
            a11 = '차이웨이 특화---------------------------\n'+menu[74].menu
            return a1 + a2 + a3 + a4 + a5+ a6+a7+a8+a9+a10+a11

        elif cafeteria_name == '복지관(교직원)':
            menu = Menu.objects.all()
            b1 = '키친1--------------------------------\n'+menu[81].menu + '\n\n\n'
            b2 = '키친2-------------------------------\n'+menu[88].menu + '\n\n\n'
            b3 = '셀러드바---------------------------\n'+menu[95].menu + '\n\n\n'
            b4 = '석식------------------\n'+menu[102].menu
            return b1 + b2 + b3 + b4
    elif week_of_day == '토':
        if cafeteria_name == '복지관(학식)':
            menu = Menu.objects.all()
            a1 = '착한아침--------------------------------\n'+menu[5].menu + '\n\n\n'
            a2 = '중식 가마-------------------------------\n'+menu[12].menu + '\n\n\n'
            a3 = '중식 누들송 면---------------------------\n'+menu[19].menu + '\n\n\n'
            a4 = '중식 누들송 카페테리아------------------\n'+menu[26].menu + '\n\n\n'
            a5 = '중식 인터쉐프----------------------------\n'+menu[33].menu + '\n\n\n'
            a6 = '중식 데일리밥----------------------------\n'+menu[40].menu + '\n\n\n'
            a7 = '석식 가마-------------------------------\n'+menu[47].menu + '\n\n\n'
            a8 = '석식 인터쉐프----------------------------\n'+menu[54].menu + '\n\n\n'
            a9 = '석식 데일리밥----------------------------\n'+menu[61].menu + '\n\n\n'
            a10 = '차이웨이 상시---------------------------\n'+menu[68].menu + '\n\n\n'
            a11 = '차이웨이 특화---------------------------\n'+menu[75].menu
            return a1 + a2 + a3 + a4 + a5+ a6+a7+a8+a9+a10+a11

        elif cafeteria_name == '복지관(교직원)':
            menu = Menu.objects.all()
            b1 = '키친1--------------------------------\n'+menu[82].menu + '\n\n\n'
            b2 = '키친2-------------------------------\n'+menu[89].menu + '\n\n\n'
            b3 = '셀러드바---------------------------\n'+menu[96].menu + '\n\n\n'
            b4 = '석식------------------\n'+menu[103].menu
            return b1 + b2 + b3 + b4

        elif cafeteria_name == '법식(한울)':
            menu = Menu.objects.all()
            c1 = '바로바로---------------------------\n'+menu[109].menu+ '\n\n\n'
            c2 = '바로바로2---------------------------\n'+menu[116].menu+ '\n\n\n'
            c3 = '면이랑---------------------------\n'+menu[123].menu+ '\n\n\n'
            c4 = '밥이랑하나-------------------------\n'+menu[130].menu+ '\n\n\n'
            c5 = '밥이랑두울-------------------------\n'+menu[137].menu+ '\n\n\n'
            c6 = '석쇠랑---------------------------\n'+menu[144].menu+ '\n\n\n'
            c7 = '석쇠랑(조식)-----------------------\n'+menu[151].menu+ '\n\n\n'
            return c1+c2+c3+c4+c5+c6+c7

    elif week_of_day == '일':
        if cafeteria_name == '복지관(학식)':
            menu = Menu.objects.all()
            a1 = '착한아침--------------------------------\n'+menu[6].menu + '\n\n\n'
            a2 = '중식 가마-------------------------------\n'+menu[13].menu + '\n\n\n'
            a3 = '중식 누들송 면---------------------------\n'+menu[20].menu + '\n\n\n'
            a4 = '중식 누들송 카페테리아------------------\n'+menu[27].menu + '\n\n\n'
            a5 = '중식 인터쉐프----------------------------\n'+menu[34].menu + '\n\n\n'
            a6 = '중식 데일리밥----------------------------\n'+menu[41].menu + '\n\n\n'
            a7 = '석식 가마-------------------------------\n'+menu[48].menu + '\n\n\n'
            a8 = '석식 인터쉐프----------------------------\n'+menu[55].menu + '\n\n\n'
            a9 = '석식 데일리밥----------------------------\n'+menu[62].menu + '\n\n\n'
            a10 = '차이웨이 상시---------------------------\n'+menu[69].menu + '\n\n\n'
            a11 = '차이웨이 특화---------------------------\n'+menu[76].menu
            return a1 + a2 + a3 + a4 + a5+ a6+a7+a8+a9+a10+a11

        elif cafeteria_name == '복지관(교직원)':
            menu = Menu.objects.all()
            b1 = '키친1--------------------------------\n'+menu[83].menu + '\n\n\n'
            b2 = '키친2-------------------------------\n'+menu[90].menu + '\n\n\n'
            b3 = '셀러드바---------------------------\n'+menu[97].menu + '\n\n\n'
            b4 = '석식------------------\n'+menu[104].menu
            return b1 + b2 + b3 + b4

        elif cafeteria_name == '법식(한울)':
            menu = Menu.objects.all()
            c1 = '바로바로---------------------------\n'+menu[110].menu+ '\n\n\n'
            c2 = '바로바로2---------------------------\n'+menu[117].menu+ '\n\n\n'
            c3 = '면이랑---------------------------\n'+menu[124].menu+ '\n\n\n'
            c4 = '밥이랑하나-------------------------\n'+menu[131].menu+ '\n\n\n'
            c5 = '밥이랑두울-------------------------\n'+menu[138].menu+ '\n\n\n'
            c6 = '석쇠랑---------------------------\n'+menu[145].menu+ '\n\n\n'
            c7 = '석쇠랑(조식)-----------------------\n'+menu[152].menu+ '\n\n\n'
            return c1+c2+c3+c4+c5+c6+c7
