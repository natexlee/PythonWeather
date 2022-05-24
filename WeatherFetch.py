import http.client
import json

locationName = input("Enter a location name:")

if (locationName != ""):
    conn = http.client.HTTPSConnection("weatherdbi.herokuapp.com")
    payload = ''
    headers = {}
    conn.request("GET", "/data/weather/" + locationName, payload, headers)
    res = conn.getresponse()
    data = res.read()
    #print(data.decode("utf-8"))
    formattedData = json.loads(data)

#print(formattedData)
print(formattedData["region"])
print(formattedData["currentConditions"]["dayhour"])
print("Temp: " + str(formattedData["currentConditions"]["temp"]["f"]) + " farenheit")
print("wind: " + str(formattedData["currentConditions"]["wind"]["mile"]) + " mph ")