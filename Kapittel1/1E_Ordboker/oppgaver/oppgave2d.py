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
brukervalg = {nummer: {"by": by, "folketall": folketall} for nummer, (by, folketall) in enumerate(byer.items(), start=1)}
print(brukervalg[1]["by"])