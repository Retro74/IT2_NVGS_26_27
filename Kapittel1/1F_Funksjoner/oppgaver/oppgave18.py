def isfloat(tekst):
    try:
        float(tekst)
        return True
    except:
        return False
def min_pc(modell:str, ram:str, lagring:str, os:str,
          prosessor:str         = "Ukjent prosessor",
          prosessorhastighet:str= "3.5 GHz",
          grafikkort:str        = "Integrert grafikk",
          skjermstorrelse:float = 15.6,
          nettverkskort:str     = "1 Gbps",
          vekt:float            = 2.0,
          **specs):
################   modell  ###############
    if not isinstance(modell, str):##Sjekker om den er satt til tekst
        print("Modell er ikke riktig beskrevet.")
        return
    if len(modell.strip()) == 0:
        print("Modell er ikke riktig beskrevet.")
        return
################   ram  ###############
    if not isinstance(ram, str):##Sjekker om den er satt til tekst
        print("Ram er ikke riktig beskrevet.")
        return
    if len(ram.strip())<4:
        if ram[-2:]!= "GB" and not ram[:-3].isnumeric():
            print("Ram er ikke riktig beskrevet.")
            return

################   lagring  ###############
    if not isinstance(lagring, str):##Sjekker om den er satt til tekst
        print("Lagring er ikke riktig beskrevet.")
        return
    if len(lagring.strip())<4:
        print("Lagring er ikke riktig beskrevet.")
        return
    if lagring[-2:] not in ["GB", "TB"]:
        print("Lagring er ikke riktig beskrevet.")
        return
    if not lagring[:-3].isnumeric():
        print("Lagring er ikke riktig beskrevet.")
        return
    if float(lagring[:-3]) == 0:
        print("Lagring er ikke riktig beskrevet.")
        return

################   os  ###############
    if os not in ["Windows 11", "Windows 10","Ubuntu", "Debian","macOS"]:
        print("Os er ikke riktig beskrevet.")
        return

################   prosessor  ###############
    if not isinstance(prosessor, str):##Sjekker om den er satt til tekst
        print("Prosessor er ikke riktig beskrevet.")
        return
    if len(prosessor.strip()) == 0:
        print("Prosessor er ikke riktig beskrevet.")
        return
################   prosessorhastighet  ###############
    if not isinstance(prosessorhastighet, str):##Sjekker om den er satt til tekst
        print("Prosessorhastighet er ikke riktig beskrevet.")
        return
   
    if len(prosessorhastighet.strip())<5:
        print("Prosessorhastighet er ikke riktig beskrevet.")
        return
    if prosessorhastighet[-3:]!= "GHz":
        print("Prosessorhastighet er ikke riktig beskrevet.")
        return
    if not isfloat(prosessorhastighet[:-5]):
        print("Prosessorhastighet er ikke riktig beskrevet.")
        return
    if not (1.0 <= float(prosessorhastighet[:-5]) <=6.0):
        print("Prosessorhastighet er ikke riktig beskrevet.")
        return
################   grafikkort  ###############
    if not isinstance(grafikkort, str):##Sjekker om den er satt til tekst
        print("Grafikkort er ikke riktig beskrevet.")
        return
    if grafikkort.strip() == "":
        print("Grafikkort er ikke riktig beskrevet.")
        return

################   skjermstorrelse  ###############
    if not isinstance(skjermstorrelse, float):##Sjekker om den er satt til tekst
        print("Skjermstorrelse er ikke riktig beskrevet.")
        return
    if not(10 <= skjermstorrelse <=40):
        print("Skjermstorrelse er ikke riktig beskrevet.")
        return

################   nettverkskort  ###############
    if nettverkskort not in ["10 Mbps", "100 Mbps", "1 Gbps"]:
        print("Nettverkskort er ikke riktig beskrevet.")
        return

################   vekt  ###############
    if not isinstance(vekt, float) and not isinstance(vekt, int):
        print("Vekt er ikke riktig beskrevet.")
        return
    if vekt <=0:
        print("Vekt er ikke riktig beskrevet.")
        return
    

    print("Alt er registert.")
    print(f"Modell: {modell}\n"
        f"Ram: {ram}\n"
        f"Lagring: {lagring}\n"
        f"Operativsystem:{os} \n"
        f"Prosessor: {prosessor}\n"
        f"Prosessorhastighet: {prosessorhastighet}\n"
        f"Grafikkort: {grafikkort}\n"
        f"Skjermstorrelse: {skjermstorrelse}\n"
        f"Nettverkskort: {nettverkskort}\n"
        f"Nettverkskort:{nettverkskort}\n"
        f"Vekt: {vekt}")
    for nokkel, verdi in specs.items():
        print(f"{nokkel.capitalize()}: {verdi}")

print("PC1")
min_pc("Dell", "4 GB","10 GB","Windows 10")

print(f"\nPC2 med en feil:")
min_pc("Lenovo Thinkpad", "16 GB","20 Gb","Ubuntu")

print(f"\nPC3 med ekstra info:")
min_pc("HP", "8 GB", "1 TB", "macOS", 
       prosessorhastighet="3.3 GHz",
       grafikkort="Ryzon 4024GXP",
       skjermstorrelse=20.6,
       nettverkskort="100 Mbps",
       farge="sort", 
       minnekortleser="Ja",
       USB_c_kontakter= 5)