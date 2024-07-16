import tkinter as tk
import requests
import json


# Replace with your own API key

api_key = "YOUR_API_KEY"

def get_weather(city):
  url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"

  response = requests.get(url)

  if response.status_code == 200:
    data = json.loads(response.text)
    return data
  else:
    print("Error:", response.status_code)
    return None


def update_weather(city):
  weather_data = get_weather(city)

  if weather_data:
    city_name = weather_data["name"]
    weather_description = weather_data["weather"][0]["description"]
    temperature = weather_data["main"]["temp"] - 273.15  # Convert Kelvin to Celsius

    city_label.config(text=city_name)
    weather_label.config(text=weather_description)
    temp_label.config(text=f"{temperature:.2f} °C")
  else:
    city_label.config(text="City Not Found")
    weather_label.config(text="")
    temp_label.config(text="")


root = tk.Tk()
root.title("Weather App")

city_label = tk.Label(root, text="City:")
city_label.pack()

weather_label = tk.Label(root, text="")
weather_label.pack()

temp_label = tk.Label(root, text="")
temp_label.pack()

city_entry = tk.Entry(root)
city_entry.pack()

update_button = tk.Button(root, text="Get Weather", command=lambda: update_weather(city_entry.get()))
update_button.pack()


root.mainloop()
