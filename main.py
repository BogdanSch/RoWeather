from pyowm import OWM
from pyowm.utils import config
import eel
import geocoder

token = 'fada024d74ea8c82c596e30e55e3f9d1'

@eel.expose
def get_weather(city):
    owm = OWM(token)
    mgr = owm.weather_manager()

    try:
        observation = mgr.weather_at_place(city)
        w = observation.weather
        temp = round(w.temperature('celsius')['temp'])
        result = f"In the city {city} is {w.detailed_status} and \n temperature is {temp}C "

        return result
    except:
        print("Place isn't found!")

if __name__ == '__main__':
    eel.init('web')
    eel.start('main.html', size=(900, 600))