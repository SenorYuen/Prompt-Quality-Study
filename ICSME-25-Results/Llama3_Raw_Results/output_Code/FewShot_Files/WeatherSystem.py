class WeatherSystem:
    """
    This is a class representing a weather system that provides functionality to query weather information for a specific city and convert temperature units between Celsius and Fahrenheit.
    """

    def __init__(self, city) -> None:
        """
        Initialize the weather system with a city name.
        """
        self.temperature = None
        self.weather = None
        self.city = city
        self.weather_list = {}

    # Query the weather system for the weather and temperature of the city, and convert the temperature units based on the input parameter.
    def query(self, weather_list, tmp_units='celsius'):
        # Check if the city exists in the weather list
        if self.city in weather_list:
            # Get the weather and temperature of the city
            self.weather = weather_list[self.city]['weather']
            self.temperature = weather_list[self.city]['temperature']
            
            # Convert the temperature units if necessary
            if tmp_units == 'fahrenheit' and weather_list[self.city]['temperature units'] == 'celsius':
                self.temperature = self.celsius_to_fahrenheit()
            elif tmp_units == 'celsius' and weather_list[self.city]['temperature units'] == 'fahrenheit':
                self.temperature = self.fahrenheit_to_celsius()
            
            # Return the temperature and weather of the city
            return self.temperature, self.weather
        else:
            # Return None if the city does not exist in the weather list
            return None

    # Set the city of the weather system.
    def set_city(self, city):
        # Update the city of the weather system
        self.city = city

    # Convert the temperature from Celsius to Fahrenheit.
    def celsius_to_fahrenheit(self):
        # Check if the temperature is not None
        if self.temperature is not None:
            # Convert the temperature from Celsius to Fahrenheit
            return (self.temperature * 9/5) + 32
        else:
            # Return None if the temperature is None
            return None

    # Convert the temperature from Fahrenheit to Celsius.
    def fahrenheit_to_celsius(self):
        # Check if the temperature is not None
        if self.temperature is not None:
            # Convert the temperature from Fahrenheit to Celsius
            return (self.temperature - 32) * 5/9
        else:
            # Return None if the temperature is None
            return None