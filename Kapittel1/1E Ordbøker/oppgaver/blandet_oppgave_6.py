from blandet_oppgave_vaerdata import vaerdata
from datetime import datetime
import requests
vaer_ikoner = {
"Clear": "☀️",
"Clouds": "☁️",
"Rain": "🌧️",
"Drizzle": "🌦️",
"Thunderstorm": "⛈️",
"Snow": "❄️",
}
vindikoner = {
"N": "⬆️",
"NØ": "↗️",
"Ø": "➡️",
"SØ": "↘️",
"S": "⬇️",
"SV": "↙️",
"V": "⬅️",
"NV": "↖️"
}
def vindikon(vindretning):
    if 337.5 <= vindretning or vindretning < 22.5:
        return vindikoner["N"]
    elif vindretning < 67.5:
        return vindikoner["NØ"]
    elif vindretning < 112.5:
        return vindikoner["Ø"]
    elif vindretning < 157.5:
        return vindikoner["SØ"]
    elif vindretning < 202.5:
        return vindikoner["S"]
    elif vindretning < 247.5:
        return vindikoner["SV"]
    elif vindretning < 292.5:
        return vindikoner["V"]
    else:
        return vindikoner["NV"]


#Henter stedsnavn ut fra latitude og longdetude
url = f"https://nominatim.openstreetmap.org/reverse?lat={vaerdata['lat']}&lon={vaerdata['lon']}&format=jsonv2"
response = requests.get(url,headers={"User-Agent": "MittProgram"})
data = response.json()


#Skriver ut værdata
print(f'Værdata for {data["address"]["city"]}, Dato: {datetime.fromtimestamp(vaerdata["hourly"][10]["dt"]).date()}')
for i in range(10,34, 4): #Her for hver 4. time
    for nokkel,verdi in vaerdata["hourly"][i].items():
        if nokkel == "dt":
            print("Klokken:", datetime.fromtimestamp(verdi).hour)
        elif nokkel in ["temp", "feels_like"]:
            print("Temperatur: ", round(verdi- 273.15), "grader")
        elif nokkel == "weather":
            print("Vær:", vaer_ikoner[verdi[0]["main"]])
        elif nokkel =="wind_speed":
            print("Vind:", verdi, "m/s")
        elif nokkel == "wind_deg":
            print("Vindretning:", vindikon(verdi))
#        else:
#            print(nokkel, verdi)
    print()
print(len(vaerdata["hourly"]))

