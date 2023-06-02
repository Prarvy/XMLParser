# Designed by Prakash Srinivasan ( prarvy@gmail.com )
# Project Name: XML Parser
# Version: 1.0: Base version by author
import xml.etree.ElementTree as Et


# Convert Celsius to Fahrenheit
class TemperatureConverter:
    @staticmethod
    def convert_celsius_to_fahrenheit(celsius):
        return round((9/5 * celsius + 32), 1)


# Parse XML Data
class ForecastXmlParser:
    @staticmethod
    def parse():
        tree = Et.parse('forecast.xml')
        root = tree.getroot()

        for item in root.findall('item'):
            day = item.find('day').text
            celsius = item.find('temperature_in_celsius').text
            fahrenheit = TemperatureConverter.convert_celsius_to_fahrenheit(float(celsius))
            print(f"{day}: {celsius} Celsius, {fahrenheit} Fahrenheit")


ForecastXmlParser.parse()
