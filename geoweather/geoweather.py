import click
import forecastio
from geopy.geocoders import Nominatim

@click.command()
@click.option('--address', help='Address String')
def process_input(address):
    """ Takes and address string and displays a weather profile """

    # geolocate address from supplied address string
    geolocator = Nominatim()
    target_location = geolocator.geocode(address)
    print "Target Location : "+target_location
    print "Co-ordinates ({0}, {1})".format(target_location.latitude, target_location.longitude)

    # Call forecastio to get weather details
    api_key = ""
    weather_forecast = forecastio.load_forecast(api_key, target_location.latitude, target_location.longitude)


if __name__ == '__main__':
    process_input()