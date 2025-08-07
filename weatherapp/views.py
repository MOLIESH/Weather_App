# from django.shortcuts import render
# from django.contrib import messages
# import requests
# import datetime


# def home(request):
   
#     if 'city' in request.POST:
#          city = request.POST['city']
#     else:
#          city = 'indore'     
    
#     url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid='
#     PARAMS = {'units':'metric'}

#     API_KEY =  ''

#     SEARCH_ENGINE_ID = ''
     
#     query = city + " 1920x1080"
#     page = 1
#     start = (page - 1) * 10 + 1
#     searchType = 'image'
#     city_url = f"https://www.googleapis.com/customsearch/v1?key={API_KEY}&cx={SEARCH_ENGINE_ID}&q={query}&start={start}&searchType={searchType}&imgSize=xlarge"

#     data = requests.get(city_url).json()
#     count = 1
#     search_items = data.get("items")
#     image_url = search_items[1]['link']
    

#     try:
          
#           data = requests.get(url,params=PARAMS).json()
#           description = data['weather'][0]['description']
#           icon = data['weather'][0]['icon']
#           temp = data['main']['temp']
#           day = datetime.date.today()

#           return render(request,'weatherapp/index.html' , {'description':description , 'icon':icon ,'temp':temp , 'day':day , 'city':city , 'exception_occurred':False ,'image_url':image_url})
    
#     except KeyError:
#           exception_occurred = True
#           messages.error(request,'Entered data is not available to API')   
#           # city = 'indore'
#           # data = requests.get(url,params=PARAMS).json()
          
#           # description = data['weather'][0]['description']
#           # icon = data['weather'][0]['icon']
#           # temp = data['main']['temp']
#           day = datetime.date.today()

#           return render(request,'weatherapp/index.html' ,{'description':'clear sky', 'icon':'01d'  ,'temp':25 , 'day':day , 'city':'indore' , 'exception_occurred':exception_occurred } )
               
    
from django.shortcuts import render
from django.contrib import messages
import requests
import datetime

def home(request):
    if 'city' in request.POST:
        city = request.POST['city']
    else:
        city = 'indore'     

    weather_url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid=Enter your Openweatherapi id'
    PARAMS = {'units': 'metric'}

    API_KEY = ''  # 🔑 Make sure to add valid API keys
    SEARCH_ENGINE_ID = ''

    # -------------------- Get image URL safely --------------------
    image_url = '/static/default.jpg'  # fallback image

    try:
        query = city + " 1920x1080"
        searchType = 'image'
        city_url = f"https://www.googleapis.com/customsearch/v1?key={API_KEY}&cx={SEARCH_ENGINE_ID}&q={query}&start=1&searchType={searchType}&imgSize=xlarge"
        search_response = requests.get(city_url)
        if search_response.status_code == 200:
            search_data = search_response.json()
            search_items = search_data.get("items")
            if search_items and len(search_items) > 1 and 'link' in search_items[1]:
                image_url = search_items[1]['link']
    except Exception as e:
        print("Image API error:", e)
        # continue with fallback image

    # -------------------- Weather data --------------------
    try:
        weather_data = requests.get(weather_url, params=PARAMS).json()
        description = weather_data['weather'][0]['description']
        icon = weather_data['weather'][0]['icon']
        temp = weather_data['main']['temp']
        day = datetime.date.today()

        return render(request, 'weatherapp/index.html', {
            'description': description,
            'icon': icon,
            'temp': temp,
            'day': day,
            'city': city,
            'exception_occurred': False,
            'image_url': image_url
        })

    except KeyError:
        messages.error(request, 'Entered data is not available to API')   
        day = datetime.date.today()
        return render(request, 'weatherapp/index.html', {
            'description': 'clear sky',
            'icon': '01d',
            'temp': 25,
            'day': day,
            'city': 'indore',
            'exception_occurred': True,
            'image_url': image_url
        })
