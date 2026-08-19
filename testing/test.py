#tegn = "#"
#for i in range(1,20,2):
#    print(f"{tegn*i:^20}")


#navn = input(f"Hva heter du?\n")
navn = "Roger"
alder=""
while type(alder)!=int:
    try: 
        alder = int(input(f"Hvor gammel er du?\n"))

    except ValueError:
        print("Skriv ett tall")
print(f"Hei, {navn} du er {alder} år")