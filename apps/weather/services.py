import random
from datetime import datetime
from .models import Weather

class WeatherService:

    @staticmethod
    def generate_key(stroke_name):
        if not stroke_name:
            return None
        stroke = stroke_name.lower().strip()
        ascii_sum = sum(ord(char) for char in stroke if char.isalpha())
        length = len(stroke)
        if len(stroke)< 3:
            first_lett='xzc'
        else: 
            first_lett = stroke[:3]
        weather_key= str(ascii_sum * length)+"_"+first_lett
        return weather_key
    @staticmethod
    def generate_weather(weather_id):
        if not weather_id:
            return None
        
        seed = hash(weather_id)

        random.seed(seed)
        month = datetime.now().month
        
        if month in [12, 1, 2]:  
            temp = random.uniform(-40, -10)
        elif month in [3, 4, 5]: 
            temp = random.uniform(-15, 15)
        elif month in [6, 7, 8]: 
            temp = random.uniform(15, 38)
        else:
            temp = random.uniform(-10, 15)
        
        weather = {
            'weather_key' :  weather_id,
            'temperature': round(temp, 1), 
            'humidity': random.randint(55, 83), 
            'pressure': random.randint(730, 785),
            'wind_speed': round(random.uniform(0.5, 15)),
            'wind_direction': random.choice(['С', 'СВ', 'В', 'ЮВ', 'Ю', 'ЮЗ', 'З', 'СЗ']),
            'source_url': 'True weather everywhere', 
        }
        random.seed()
        return weather
    
    @staticmethod   
    def get_weather(loc_key):
        weather_record = Weather.objects.filter(
            weather_key = loc_key,
            ).first()
        if not weather_record :
            weather = WeatherService.generate_weather(loc_key)
            weather_record = Weather.objects.create(**weather)
        return weather_record
    
    @staticmethod
    def up_weather(stroke_name):
        if not stroke_name:
            return None
        loc_key = WeatherService.generate_key(stroke_name)
        return WeatherService.get_weather(loc_key)
       