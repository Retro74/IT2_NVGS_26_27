elev = {
    "Fornavn": "Morten",
    "Etternavn":"Olsen",
    "Klasse": "2STC",
    "e-post": "morten.olsen@gmail.com"
}

#print(elev["Fornavn"])
#print(elev)
elev["Klasse"]= "3STC"
#print(elev["Klasse"])
elev["Telefonnummer"] = 91912345
#print(elev["Telefonnummer"])
#del elev["Telefonnummer"]
#elev.pop("Telefonnummer")
#print(elev["Telefonnummer"])

#del elev["e-post"]
if "e-post" in elev:
    print(f"E-post er registert med verdien {elev['e-post']}")
else:
    print("Epost er ikke registert på eleven.")

#del elev["Telefonnummer"]
#print(elev.get("Telefonnummer", "Ikke registert"))

#print("Vi har registrert eleven med:")
#for nokkel, verdi in elev.items():
#    print(f"{nokkel}: {verdi}")


elever = [
    {"Navn": "Ole",     "Telefonnummer": 12345678},
    {"Navn": "Lise",    "Telefonnummer": 23456789},
    {"Navn": "Ola",     "Telefonnummer": 98765432},
]

#for elev in elever:
#    print(f'{elev["Navn"]}, Telefonnummer {elev["Telefonnummer"]}')


bytemperaturer = {"Oslo": 22,
                  "Bergen": 17,
                   "Trondheim": 14,
                   "Stavanger": 20,
                   "Kristiansand": 23,
                   "Tromsø": 12}

##Sortere på nøkkel
#for by in sorted(bytemperaturer.keys()):
#    print(f"{by} har {bytemperaturer[by]} grader i dag.")

#Sorter etter verdi
#for by, temp in sorted(
#    bytemperaturer.items(), 
#    key=lambda by_temp:by_temp[1], 
#    reverse=True):
#    print(f"{by} har {temp} grader i dag")


vaer = {
    "Oslo": {
        "Temperatur": 22,
        "Nedbør": 0,
        "Vindstyrke": 5,
        "Vindretning": "S",
        "emoji":"☀️"
    },
    "Tromsø": {
        "Temperatur": 12,
        "Nedbør": 6,
        "Vindstyrke": 3,
        "Vindretning": "SV",
        "emoji": "☁️"
    },
    "Bergen": {
        "Temperatur": 14,
        "Nedbør": 16,
        "Vindstyrke": 4,
        "Vindretning": "V",
        "emoji": "🌧️"
    }
}


#print(f'I Bergen er det {vaer["Bergen"]["emoji"]}  {vaer["Bergen"]["Temperatur"]} grader og {vaer["Bergen"]["Nedbør"]} mm nedbør.')
#for by, data in sorted(vaer.items(), key=lambda vaer[by]: data["Temperatur"]):
#    print(by, data)


elev1 = {"navn": "Ola"}
elev2 = elev1.copy()
elev1["navn"] = "Morten"
#print(elev2["navn"])

from copy import deepcopy
vaer2 = deepcopy(vaer)
vaer["Oslo"]["Temperatur"]= 0
#print(f'{vaer2["Oslo"]["Temperatur"]}')


hoyeste_temp = max(bytemperaturer, key=bytemperaturer.get)
#print(f"Høyeste temp er {hoyeste_temp}")


koder = ["NO", "SE", "DK"]
land_navn = ["Norge", "Sverige", "Danmark"]
kode_land = dict(zip(koder, land_navn))

landskoder = list(kode_land.keys())
print(landskoder)
#print(f"DK er: {kode_land['DK']}")

#land = {
#    "NO": "Norge",
#    "SE": "Sverige",
#    "DK": "Danmark"}
land_koder = {navn:kode for kode,navn in kode_land.items()}

#print(f"Norge har koden: {land_koder['Norge']}")
bytemperaturer = {"Oslo": 22,
                  "Bergen": 17,
                   "Trondheim": 14,
                   "Stavanger": 20,
                   "Kristiansand": 23,
                   "Tromsø": 12}

#Dictionary comprehention (filtering)
varme_byer = {by:temp for by, temp in bytemperaturer.items() if temp>=15} 

print (varme_byer)