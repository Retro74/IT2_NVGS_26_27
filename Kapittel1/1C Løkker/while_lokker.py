

#ant_repetisjoner = int(input("Hvor mange repetisjoner vil de ha? "))

#import os
#passord = ""

#while passord != "incorrect":
#    passord=input("Type your password: ")
#    print("Your password is incorrect")
#os.system("cls")
#print("Login success!")



while True:

    kommando =input("Hva skal vi gjøre? ")
    if kommando == "regnut":
        print (4+4)
    elif kommando =="avslutt":
        break ##Hopper ut av sløyfen
    elif kommando == "neste":
        continue ## Dropper resten av denne runden men forstetter kjøring av løkke
    else:
        print("Vi fortsetter")

    print("Programmet fortsetter en runden til")

print("Programmet avslutter")
