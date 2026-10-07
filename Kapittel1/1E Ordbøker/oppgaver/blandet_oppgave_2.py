tall_tekst = {
    0:"null",    1:"en",    2:"to",
    3:"tre",    4:"fire",    5:"fem",
    6:"seks",    7:"sju",    8:"åtte",
    9:"ni",    10:"ti",
}

#a)
print(f"+{'-'*4:4}+{'-'*6:6}+")
for tall, tekst in tall_tekst.items():
    print(f"|{tall:4}|{tekst:6}|") 
print(f"+{'-'*4:4}+{'-'*6:6}+")

#b)
while True:
    tall = input("Skriv inn ett tall mellom 0-10 (q=quit): ")
    if tall.isdigit():
        tall = int(tall)
        if 0<=tall<=10:
            print(f"Du skrev tallet {tall_tekst[tall]}")
        else:
            print("Tallet er ikke mellom 0-10")
    elif tall == "q":
        break
    else:
        print("Du skrev ikke et tall.")