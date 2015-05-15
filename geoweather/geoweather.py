import click
import forecastio
from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut
from prettytable import PrettyTable


def fetch_api_key():
    with open("apikey.txt") as datafile:
        return datafile.readlines()[0]


@click.command()
@click.option('--location', help='Address String or Zipcode')
def process_input(location):
    """ Takes and address string and displays a weather profile """

    # geolocate address from supplied address string
    geolocator = Nominatim()
    try:
        target_location = geolocator.geocode(location, timeout=5)
        print "Target Location : " + target_location.address
        print "Co-ordinates ({0}, {1})".format(target_location.latitude, target_location.longitude)
    except GeocoderTimedOut:
        print "Error: Geocode failed due to timeout. Please try again in a few minutes"

    # Load API key
    api_key = fetch_api_key()

    # Load weather for location provided
    weather_forecast = forecastio.load_forecast(api_key, target_location.latitude, target_location.longitude)

    # Process Current weather
    hourly_weather = weather_forecast.hourly()
    hourly_table = PrettyTable()

    for hourly_data in hourly_weather.data[0:5]:
        hourly_table.add_column(hourly_data.time.strftime('%H:%M:%S'), [hourly_data.summary])
    print "Current Weather:"
    print hourly_table

    # Process weekly forecast
    daily_weather = weather_forecast.daily()
    forecast_table = PrettyTable(["Date", "Forecast Summary"])
    for daily_data in daily_weather.data:
        forecast_table.add_row([daily_data.time.strftime('%m/%d/%Y'), daily_data.summary])
    print "Forecast for the next few days"
    print forecast_table


if __name__ == '__main__':
    process_input()