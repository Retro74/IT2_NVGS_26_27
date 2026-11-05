eliteserielag = [
  { "lag": "Lillestrøm", "seriemesterskap": [1976, 1977, 1986, 1989], "norgesmesterskap": [1977, 1978, 1981, 1985, 2007, 2017] },
  { "lag": "Molde", "seriemesterskap": [2011, 2012, 2014, 2019], "norgesmesterskap": [1994, 2005, 2013, 2014, 2021] },
  { "lag": "Viking", "seriemesterskap": [1972, 1973, 1974, 1975, 1979, 1982, 1991], "norgesmesterskap": [1979, 1989, 2001, 2019] },
  { "lag": "Strømsgodset", "seriemesterskap": [1970, 2013], "norgesmesterskap": [1969, 1970, 1973, 1991, 2010] },
  { "lag": "Aalesund", "seriemesterskap": [], "norgesmesterskap": [2009, 2011] },
  { "lag": "Rosenborg", "seriemesterskap": [1967, 1969, 1971, 1985, 1988, 1990, 1992, 1993, 1994, 1995, 1996, 1997, 1998, 1999, 2000, 2001, 2002, 2003, 2004, 2006, 2009, 2010, 2015, 2016, 2017, 2018], "norgesmesterskap": [1964, 1971, 1988, 1990, 1992, 1995, 1999, 2003, 2015, 2016, 2018] },
  { "lag": "Sarpsborg", "seriemesterskap": [], "norgesmesterskap": [] },
  { "lag": "Bodø/Glimt", "seriemesterskap": [2020, 2021], "norgesmesterskap": [1975, 1993] },
  { "lag": "Odd", "seriemesterskap": [], "norgesmesterskap": [2000] },
  { "lag": "Tromsø", "seriemesterskap": [], "norgesmesterskap": [1986, 1996] },
  { "lag": "Vålerenga", "seriemesterskap": [1965, 1981, 1983, 1984, 2005], "norgesmesterskap": [1980, 1997, 2002, 2008] },
  { "lag": "HamKam", "seriemesterskap": [], "norgesmesterskap": [] },
  { "lag": "Sandefjord", "seriemesterskap": [], "norgesmesterskap": [] },
  { "lag": "Haugesund", "seriemesterskap": [], "norgesmesterskap": [] },
  { "lag": "Jerv", "seriemesterskap": [], "norgesmesterskap": [] },
  { "lag": "Kristiansund", "seriemesterskap": [], "norgesmesterskap": [] }
]

#a) og d) 
#Filterer for minst ett seriemesterskap, sortert og printet
eliteserielag_minst_ett_seriemesterskap = [lag for lag in eliteserielag if len(lag["seriemesterskap"])>0]
eliteserielag_minst_ett_seriemesterskap.sort(key=lambda lag:len(lag["seriemesterskap"]), reverse = True)
print("Oversikt over seriemesterskap:")
for lag in eliteserielag_minst_ett_seriemesterskap:
    print(f'{lag["lag"]} har {len(lag["seriemesterskap"])} seriesmesterskap')

#Enklere utgave
#for laget in eliteserielag:
#    if len(laget["seriemesterskap"])>0:
#        print(f'{laget["lag"]} har {len(laget["seriemesterskap"])} seriesmesterskap')

print()
#b) og e)
#Filterer for minst ett norgesmesterskap, sortert og printet
eliteserielag_minst_ett_norgesmesterskap = [lag for lag in eliteserielag if len(lag["norgesmesterskap"])>0]
eliteserielag_minst_ett_norgesmesterskap.sort(key=lambda lag:len(lag["norgesmesterskap"]), reverse = True)
print("Oversikt over norgesmesterskap:")
for lag in eliteserielag_minst_ett_norgesmesterskap:
    print(f'{lag["lag"]} har {len(lag["norgesmesterskap"])} norgesmesterskap')


print()
#c)
#Filterer for minst ett seriemesterskap og ett norgesmesterskap, sortert og printet
eliteserielag_minst_ett_seriemesterskap_norgesmesterskap = [lag for lag in eliteserielag if len(lag["norgesmesterskap"])>0 and len(lag["seriemesterskap"])>0]
eliteserielag_minst_ett_seriemesterskap_norgesmesterskap.sort(key=lambda lag:len(lag["norgesmesterskap"])+ len(lag["seriemesterskap"]), reverse = True)
print("Oversikt over norgesmesterskap og seriemesterskap:")
for lag in eliteserielag_minst_ett_seriemesterskap_norgesmesterskap:
    print(f'{lag["lag"]} har tilsammen {len(lag["norgesmesterskap"])+ len(lag["seriemesterskap"])} norgesmesterskap og seriemesterskap')


#f) Finner første gang og siste gang serien ble vunnet 
forste_serie_aar = min(eliteserielag[0]["seriemesterskap"])
forste_serie_lag = eliteserielag[0]["lag"]
siste_serie_aar = max(eliteserielag[0]["seriemesterskap"])
siste_serie_lag = eliteserielag[0]["lag"]

for lag in eliteserielag:
    if len(lag["seriemesterskap"])==0:
        continue
    if forste_serie_aar >  min(lag["seriemesterskap"]):
        forste_serie_aar =  min(lag["seriemesterskap"])
        forste_serie_lag = lag["lag"]
    if siste_serie_aar < max(lag["seriemesterskap"]):
        siste_serie_aar = max(lag["seriemesterskap"])
        siste_serie_lag = lag["lag"]

print()
print(f"Serien ble første gang vunnet av {forste_serie_lag} i {forste_serie_aar}.")
print(f"Serien ble siste gang vunnet av {siste_serie_lag} i {siste_serie_aar}.")
