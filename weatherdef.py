import requests
city = 'Voronezh'

url = 'http://api.openweathermap.org/data/2.5/weather?q=Voronezh&appid=31f582531f85d61e2921c407f48a681c&lang=ru&units=metric'
res = requests.get(url)
data = res.json()

description = data['weather'][0]['description']
temp = data['main']['temp']

def weather(day):
    global temp
    global description
    if day == 'today':
        returntemp = str(round(temp)) + '°'
        output = returntemp + ', ' + description
        return output
print(weather('today'))