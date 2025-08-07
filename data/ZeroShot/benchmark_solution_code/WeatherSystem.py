'''
# This is a class representing a weather system that provides functionality to query weather information for a specific city and convert temperature units between Celsius and Fahrenheit.

class WeatherSystem:
    def __init__(self, city) -> None:
        """
        Initialize the weather system with a city name.
        """

    def query(self, weather_list, tmp_units = 'celsius'):
        """
        Query the weather system for the weather and temperature of the city,and convert the temperature units based on the input parameter.
        :return: the temperature and weather of the city, tuple.

        """

    def set_city(self, city):
        """
        Set the city of the weather system.
        :return: None

        """

    def celsius_to_fahrenheit(self):
        """
        Convert the temperature from Celsius to Fahrenheit.
        :return: the temperature in Fahrenheit, float.

        """

    def fahrenheit_to_celsius(self):
        """
        Convert the temperature from Fahrenheit to Celsius.
        :return: the temperature in Celsius, float.

        """
'''

class WeatherSystem:
    def __init__(self, city) -> None:
        self.temperature = None
        self.weather = None
        self.city = city
        self.weather_list = {}
    
    def query(self, weather_list, tmp_units = 'celsius'):
        self.weather_list = weather_list
        if self.city not in weather_list:
            return False
        else:
            self.temperature = self.weather_list[self.city]['temperature']
            self.weather = self.weather_list[self.city]['weather']
        if self.weather_list[self.city]['temperature units'] != tmp_units:
            if tmp_units == 'celsius':
                return self.fahrenheit_to_celsius(), self.weather
            elif tmp_units == 'fahrenheit':
                return self.celsius_to_fahrenheit(), self.weather
        else:
            return self.temperature, self.weather
    
    def set_city(self, city):
        self.city = city

    def celsius_to_fahrenheit(self):
        return (self.temperature * 9/5) + 32

    def fahrenheit_to_celsius(self):
        return (self.temperature - 32) * 5/9
