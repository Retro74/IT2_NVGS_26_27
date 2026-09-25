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
}

nede_grense     = 60_000  #int(input("Nedre grense: "))
ovre_grense     = 100_000 #int(input("Øvre grense: "))
print(f"Byer med innbyggertall mellom {nede_grense} og {ovre_grense}:")

for by, innbyggertall in byer.items():
    if nede_grense < innbyggertall < ovre_grense: 
        print(f"{by} som har {innbyggertall}")
        