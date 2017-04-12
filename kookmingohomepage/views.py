from django.shortcuts import render
from django.views.generic import TemplateView,ListView,DetailView
from .models import *
from bs4 import BeautifulSoup
from urllib.request import urlopen
from django.views.generic.edit import CreateView
from .forms import UserCreationForm
from django.core.urlresolvers import reverse_lazy

class HomeView(TemplateView):
    template_name = 'kookmingohomepage/home.html'

class HanulLV(ListView):
    model = Hanul
    template_name = 'kookmingohomepage/hanul.html'

class StudentLV(ListView):
    model = Student
    template_name = 'kookmingohomepage/student.html'

class StaffLV(ListView):
    model = Staff
    template_name = 'kookmingohomepage/staff.html'

class SmellLV(ListView):
    model = Smell
    template_name = 'kookmingohomepage/smell.html'

class DormitoryNormalLV(ListView):
    model = DormitoryNormal
    template_name = 'kookmingohomepage/normal.html'

class DormitoryRoutineLV(ListView):
    model = DormitoryRoutine
    template_name = 'kookmingohomepage/routine.html'





class UserCreateView(CreateView):
    template_name = 'registration/register.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('register_done')

class UserCreateDoneTV(TemplateView):
    template_name = 'registration/register_done.html'




def crawl(request):
    hanul= urlopen('http://kmucoop.kookmin.ac.kr/restaurant/restaurant.php?w=1')
    hanulsource = hanul.read()
    hanul.close()
    hanulsoup = BeautifulSoup(hanulsource,"lxml")

    student = urlopen('http://kmucoop.kookmin.ac.kr/restaurant/restaurant.php?w=2')
    studentsource = student.read()
    student.close()
    studentsoup = BeautifulSoup(studentsource,"lxml")

    staff= urlopen('http://kmucoop.kookmin.ac.kr/restaurant/restaurant.php?w=3')
    staffsource = staff.read()
    staff.close()
    staffsoup = BeautifulSoup(staffsource,"lxml")

    smell = urlopen('http://kmucoop.kookmin.ac.kr/restaurant/restaurant.php?w=4')
    smellsource = smell.read()
    smell.close()
    smellsoup = BeautifulSoup(smellsource,"lxml")

    normal= urlopen('http://kmucoop.kookmin.ac.kr/restaurant/restaurant.php?w=5')
    normalsource = normal.read()
    normal.close()
    normalsoup = BeautifulSoup(normalsource,"lxml")

    routine= urlopen('http://kmucoop.kookmin.ac.kr/restaurant/restaurant.php?w=6')
    routinesource = routine.read()
    routine.close()
    routinesoup = BeautifulSoup(routinesource,"lxml")


    hanultable = hanulsoup.find_all("td", class_="ft_mn")
    studenttable = studentsoup.find_all("td", class_="ft_mn")
    stafftable = staffsoup.find_all("td", class_="ft_mn")
    smelltable = smellsoup.find_all("td", class_="ft_mn")
    normaltable = normalsoup.find_all("td", class_="ft_mn")
    routinetable = routinesoup.find_all("td", class_="ft_mn")
    i = 0
    j = 0
    k = 0
    x = 0
    y = 0
    z = 0
    for tt in hanultable:
        str = hanultable[i].get_text()
        newstr = str.replace("\n",'')
        int = newstr.find('￦')
        front = newstr[0:int]
        back = newstr[int:-1]
        tt[i] = front + '\n' +back +'0'
        Hanul.objects.create(
            cafe_name = 'dd',
            time = 'dd',
            menu = tt[i]
        )
        i=i+1

    for tt in studenttable:
        str = studenttable[j].get_text()
        newstr = str.replace("\n",'')
        int = newstr.find('￦')
        front = newstr[0:int]
        back = newstr[int:-1]
        tt[j] = front + '\n' +back +'0'
        Student.objects.create(
            cafe_name = 'dd',
            time = 'dd',
            menu = tt[j]
        )
        j=j+1

    for tt in stafftable:
        str = stafftable[k].get_text()
        newstr = str.replace("\n",'')
        int = newstr.find('￦')
        front = newstr[0:int]
        back = newstr[int:-1]
        tt[k] = front + '\n' +back +'0'
        Staff.objects.create(
            cafe_name = 'dd',
            time = 'dd',
            menu = tt[k]
        )
        k=k+1

    for tt in smelltable:
        str = smelltable[x].get_text()
        newstr = str.replace("\n",'')
        int = newstr.find('￦')
        front = newstr[0:int]
        back = newstr[int:-1]
        tt[x] = front + '\n' +back +'0'
        Smell.objects.create(
            cafe_name = 'dd',
            time = 'dd',
            menu = tt[x]
        )
        x=x+1

    for tt in normaltable:
        str = normaltable[y].get_text()
        newstr = str.replace("\n",'')
        int = newstr.find('￦')
        front = newstr[0:int]
        back = newstr[int:-1]
        tt[y] = front + '\n' +back +'0'
        DormitoryNormal.objects.create(
            cafe_name = 'dd',
            time = 'dd',
            menu = tt[y]
        )
        y=y+1

    for tt in routinetable:
        str = routinetable[z].get_text()
        newstr = str.replace("\n",'')
        int = newstr.find('￦')
        front = newstr[0:int]
        back = newstr[int:-1]
        tt[z] = front + '\n' +back +'0'
        DormitoryRoutine.objects.create(
            cafe_name = 'dd',
            time = 'dd',
            menu = tt[z]
        )
        z=z+1

def delete(request):
    menu_db = Hanul.objects.all()
    menu_db.delete()

# Create your views here.
