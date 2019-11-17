import requests

from secrets import app_id

# def weather():
#     print(">> Execut logica super complicata")
#     w = {"Cluj": 15}
#     return w

def weather():
    url = f"http://api.openweathermap.org/data/2.5/weather?q=Cluj-Napoca&appid={app_id}&units=metric"
    response = requests.get(url)
    weather_cluj = response.json()
    print(">>", weather_cluj)
    temp_cluj = weather_cluj["main"]["temp"]
    return {"Cluj-Napoca": round(temp_cluj)}