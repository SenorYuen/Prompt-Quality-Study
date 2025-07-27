class WeatherSystem:
    def __init__(self, city) -> None:
        """
        Initialize the weather system with a city name.
        """
        self.city = city
        self.temperature = None
        self.weather = None

    def query(self, weather_list, tmp_units='celsius'):
        """
        Query the weather system for the weather and temperature of the city,
        and convert the temperature units based on the input parameter.
        
        :param weather_list: List of dictionaries containing weather info for cities.
        :param tmp_units: Desired temperature units ('celsius' or 'fahrenheit').
        :return: Tuple containing the temperature and weather of the city.
        """
        for weather_info in weather_list:
            if weather_info['city'].lower() == self.city.lower():
                self.temperature = weather_info['temperature']
                self.weather = weather_info['weather']
                
                if tmp_units.lower() == 'fahrenheit':
                    self.temperature = self.celsius_to_fahrenheit(self.temperature)
                
                return self.temperature, self.weather
        
        return None

    def set_city(self, city):
        """
        Set the city of the weather system.
        
        :param city: Name of the city to set.
        :return: None
        """
        self.city = city

    def celsius_to_fahrenheit(self, celsius_temp):
        """
        Convert the temperature from Celsius to Fahrenheit.
        
        :param celsius_temp: Temperature in Celsius to convert.
        :return: Temperature in Fahrenheit, float.
        """
        return (celsius_temp * 9/5) + 32

    def fahrenheit_to_celsius(self, fahrenheit_temp):
        """
        Convert the temperature from Fahrenheit to Celsius.
        
        :param fahrenheit_temp: Temperature in Fahrenheit to convert.
        :return: Temperature in Celsius, float.
        """
        return (fahrenheit_temp - 32) * 5/9