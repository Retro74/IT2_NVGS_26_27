setning = "Det var en gang en gutt som het Jens."

bokstaver = {}
for tegn in setning:
    if bokstaver.get(tegn):
        bokstaver[tegn]+=1
    else:
        bokstaver[tegn]=1

for tegn, antall in sorted(
    bokstaver.items(), 
    key=lambda tegn_antall:tegn_antall[1], 
    reverse=True):
    print(f"Tegnet: \"{tegn}\" oppter {antall} ganger")
