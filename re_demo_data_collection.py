import requests

url = "https://zillow56.p.rapidapi.com/property"

querystring = {"url":"https://www.zillow.com/homedetails/2911-Deer-Hollow-Way-UNIT-221-Fairfax-VA-22031/60391378_zpid/"}

headers = {
	"X-RapidAPI-Key": "da8bc74f10msh9f4475b257da021p12fcd9jsn011367851c30",
	"X-RapidAPI-Host": "zillow56.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

print(response.json())

url = "https://zillow56.p.rapidapi.com/similar_properties"

querystring = {"url":"https://www.zillow.com/homedetails/2911-Deer-Hollow-Way-UNIT-221-Fairfax-VA-22031/60391378_zpid/"}

headers = {
	"X-RapidAPI-Key": "da8bc74f10msh9f4475b257da021p12fcd9jsn011367851c30",
	"X-RapidAPI-Host": "zillow56.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

print(response.json())

url = "https://zillow56.p.rapidapi.com/similar_sold_properties"

querystring = {"url":"https://www.zillow.com/homedetails/2911-Deer-Hollow-Way-UNIT-221-Fairfax-VA-22031/60391378_zpid/"}

headers = {
	"X-RapidAPI-Key": "da8bc74f10msh9f4475b257da021p12fcd9jsn011367851c30",
	"X-RapidAPI-Host": "zillow56.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

print(response.json())