class WeatherData:
    def __init__(self, temperature, humidity, rainfall):
        self.temperature = temperature
        self.humidity = humidity
        self.rainfall = rainfall

    def show_weather_data(self):
        print("Weather Data")
        print(f"Temperature: {self.temperature}")
        print(f"Humidity: {self.humidity}")
        print(f"Rainfall: {self.rainfall}")
