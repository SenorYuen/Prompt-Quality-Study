class WeatherSystem:
    def __init__(self, city) -> None:
        self.temperature = None
        self.weather = None
        self.city = city
        self.weather_list = {}

    def query(self, weather_list, tmp_units='celsius'):
        self.weather_list = weather_list
        if self.city in self.weather_list:
            city_weather = self.weather_list[self.city]
            self.weather = city_weather['weather']
            self.temperature = city_weather['temperature']
            if city_weather['temperature units'] != tmp_units:
                if tmp_units == 'fahrenheit':
                    self.temperature = self.celsius_to_fahrenheit()
                else:
                    self.temperature = self.fahrenheit_to_celsius()
            return (self.temperature, self.weather)
        return None

    def set_city(self, city):
        self.city = city

    def celsius_to_fahrenheit(self):
        return (self.temperature * 9/5) + 32

    def fahrenheit_to_celsius(self):
        return (self.temperature - 32) * 5/9