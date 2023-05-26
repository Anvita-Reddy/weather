from django.shortcuts import render
from django.http import HttpResponse
import datetime
import requests
# Create your views here.


def weathers(request):
    city = request.GET.get('city','Delhi')
    ttimes = datetime.datetime.now()
    days= datetime.datetime.now()
    all = (ttimes.strftime("%H:%M"))
    dayaa =(days.strftime("%A, %d %B %Y"))
    prine = (ttimes.strftime("%p"))
    print(dayaa)


    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid=c7b6088a27aa3eccde2f52c4c4de8354"
    data = requests.get(url).json()
    
    weatherreport = {
        'city':data['name'],
        'timezone':data['timezone'],
        'weather':data['weather'][0]['main'],
        'icon':data['weather'][0]['icon'],
        'kaltemp':data['main']['temp'],
        'temp':int(data['main']['temp'] - 273),
        'humidity':data['main']['humidity'],
        'pressure':data['main']['pressure'],
        'desc':data['weather'][0]['description'],
        'windspeed':int(data['wind']['speed']*10),
        'visibility':int(data['visibility']/1000),
        'tme':all,
        'ampm':dayaa,
        'pss':prine,
    }

    context ={'data':weatherreport}
    # print(context)
    # if weatherreport['weather'] == 'Haze':
    #     return render(request,'Dust.html',context)
    

    return render(request, 'weatherhome.html',context)
#return HttpResponse("Hello Wather")
