import urllib2
import json


class WeatherData:

	def __init__(self, zip_code):
		self.zip_code = zip_code
		self.apikey = '295d4c0b86995e34a7c916df9b7dd7c7'
		self.weatherurl = 'http://api.openweathermap.org/data/2.5/weather?zip=04260,us&APPID=295d4c0b86995e34a7c916df9b7dd7c7'
	
	def GetCurrentTemp(self):
		
		response = urllib2.urlopen(self.weatherurl)
		data = json.load(response)
		self.ktemp = data["main"]["temp"]
		self.CalculateTemp()
		print("Current temp in {0} is: {1}".format(data["name"], self.temp))


	def CalculateTemp(self):
		self.temp = float(self.ktemp)*(9.0/5.0) - 459.67
