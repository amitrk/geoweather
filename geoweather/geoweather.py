import click
import forecastio
from geopy.geocoders import Nominatim


def fetch_api_key():
    with open("apikey.txt") as datafile:
        return datafile.readlines()[0]


@click.command()
@click.option('--address', help='Address String')
def process_input(address):
    """ Takes and address string and displays a weather profile """

    # geolocate address from supplied address string
    geolocator = Nominatim()
    target_location = geolocator.geocode(address, timeout=5)
    print "Target Location : "+target_location.address
    print "Co-ordinates ({0}, {1})".format(target_location.latitude, target_location.longitude)

    # Call forecastio to get weather details
    api_key = fetch_api_key()
    print api_key

    weather_forecast = forecastio.load_forecast(api_key, target_location.latitude, target_location.longitude)

    hourly_weather = weather_forecast.hourly()
    daily_weather = weather_forecast.daily()

    for hourly_data in hourly_weather.data:
        print hourly_data

    for daily_data in daily_weather.data:
        print daily_data


if __name__ == '__main__':
    process_input()