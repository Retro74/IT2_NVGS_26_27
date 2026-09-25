byer = {
    "Oslo"                  :1_043_168,
    "Bergen"	            :265_470,
    "Stavanger/Sandnes"	    :229_911,
    "Trondheim"	            :191_771,
    "Fredrikstad/Sarpsborg" :117_663,
    "Drammen"               :110_236,
    "Porsgrunn/Skien"       :94_102,
    "Kristiansand"          :64_913,
    "Ålesund"               :54_399,
    "Tønsberg"              :53_818,
    "Harstad"               :21_602,
}
byindeks = {nummer:by for nummer, by in enumerate(byer.keys(), start=1)}
for nr, by in byindeks.items():
    print(f'{nr}) {by}') 
valgtby = int(input(f"Velg by (skriv et  tall mellom 1 og {len(byindeks)})\n"))

if not valgtby in byindeks:
    print("Ukjent by.")
    exit()

print(f"Informasjon om {byindeks[valgtby]}: Innbyggertall: {byer[byindeks[valgtby]]}")