class WeatherSystem:
    def __init__(self, city):
        self.temperature = None
        self.weather = None
        self.city = city
        self.weather_list = {}

    def query(self, weather_list, tmp_units='celsius'):
        if self.city in weather_list:
            self.weather = weather_list[self.city]['weather']
            self.temperature = weather_list[self.city]['temperature']
            if tmp_units == 'fahrenheit' and weather_list[self.city]['temperature units'] == 'celsius':
                self.temperature = self.celsius_to_fahrenheit()
            elif tmp_units == 'celsius' and weather_list[self.city]['temperature units'] == 'fahrenheit':
                self.temperature = self.fahrenheit_to_celsius()
            return (self.temperature, self.weather)
        else:
            return None

    def set_city(self, city):
        self.city = city

    def celsius_to_fahrenheit(self):
        if self.temperature is not None:
            return (self.temperature * 9/5) + 32
        else:
            return None

    def fahrenheit_to_celsius(self):
        if self.temperature is not None:
            return (self.temperature - 32) * 5/9
        else:
            return None