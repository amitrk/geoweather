# Readme
A simple command line script to get current weather and forecast for the coming week

## Requirements
1. Install requirements from requirements.txt
2. Get an API key from http://developer.forecast.io

## How to use
Usage
python geoweather.py --location <address or zip>

For help
python geoweather.py --help

## Sample Output

    Target Location : None, TO, PIE, Italia
    Co-ordinates (44.933143, 7.540121)
    Current Weather:
    +------------+------------+------------+------------+----------+
    |  22:00:00  |  23:00:00  |  00:00:00  |  01:00:00  | 02:00:00 |
    +------------+------------+------------+------------+----------+
    | Light Rain | Light Rain | Light Rain | Light Rain |   Rain   |
    +------------+------------+------------+------------+----------+
    Forecast for the next few days
    +------------+----------------------------------------+
    |    Date    |            Forecast Summary            |
    +------------+----------------------------------------+
    | 05/14/2015 |        Rain throughout the day.        |
    | 05/15/2015 |      Light rain until afternoon.       |
    | 05/16/2015 |       Clear throughout the day.        |
    | 05/17/2015 |     Partly cloudy until afternoon.     |
    | 05/18/2015 | Light rain starting in the afternoon.  |
    | 05/19/2015 | Mostly cloudy starting in the evening. |
    | 05/20/2015 |      Mostly cloudy until evening.      |
    | 05/21/2015 |  Light rain starting in the evening.   |
    +------------+----------------------------------------+

## Miscellaneous
Inspired by http://www.reddit.com/r/Python/comments/34xlou/what_are_some_fun_apis_and_libraries_to_screw/cqz1c3f 
and https://github.com/jhwhite/pyweather