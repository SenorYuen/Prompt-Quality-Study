class WeatherSystem:
    def __init__(self, city) -> None:
        # Initialize the city name and temperature in Celsius
        self.city = city
        self.temperature_celsius = None
        self.weather = None

    def query(self, weather_list, tmp_units='celsius'):
        # Query the weather system for the weather and temperature of the city
        for weather in weather_list:
            if weather['city'] == self.city:
                self.weather = weather['weather']
                self.temperature_celsius = weather['temperature_celsius']
                break
        
        # Convert the temperature units based on the input parameter
        if tmp_units == 'celsius':
            return self.temperature_celsius, self.weather
        elif tmp_units == 'fahrenheit':
            return self.celsius_to_fahrenheit(), self.weather
        else:
            raise ValueError("Invalid temperature unit. Please use 'celsius' or 'fahrenheit'.")

    def set_city(self, city):
        # Set the city of the weather system
        self.city = city
        self.temperature_celsius = None
        self.weather = None

    def celsius_to_fahrenheit(self):
        # Convert the temperature from Celsius to Fahrenheit
        if self.temperature_celsius is not None:
            return (self.temperature_celsius * 9/5) + 32
        else:
            raise ValueError("Temperature not available. Please query the weather system first.")

    def fahrenheit_to_celsius(self, temperature_fahrenheit):
        # Convert the temperature from Fahrenheit to Celsius
        return (temperature_fahrenheit - 32) * 5/9


# Example usage:
weather_list = [
    {'city': 'New York', 'weather': 'Sunny', 'temperature_celsius': 25},
    {'city': 'Los Angeles', 'weather': 'Cloudy', 'temperature_celsius': 22},
]

weather_system = WeatherSystem('New York')
print(weather_system.query(weather_list))  # Output: (25, 'Sunny')
print(weather_system.query(weather_list, tmp_units='fahrenheit'))  # Output: (77.0, 'Sunny')