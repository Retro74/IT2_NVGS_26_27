import math
def radius_fra_diameter (f_diameter):
    return f_diameter/2

def omkrets_sirkel(f_radius):
    return 2*math.pi*f_radius

def areal_sirkel(f_radius):
    return math.pi*f_radius**2

def er_tall(tekst):
    try:
        float(tekst)
        return True
    except ValueError:
        return False

#diameter = float(input("Oppgi sirkelens diameter: "))
#omkrets =  omkrets_sirkel(radius_fra_diameter(diameter))
#print(f"Sirkelens omkrest er {omkrets:.2f}")

omregning = {
    "r": lambda verdi: verdi,      # radius oppgis allerede
    "d": radius_fra_diameter       # må regnes om til radius
}

brukerinput = input(f"Regn ut areal av en sirkel.\n"
                    f"Oppgi sirkelens dimater eller raius.\n"
                    f"Skriv f.eks. r=12, eller d=24:\n")

if brukerinput[:2] not in ["r=", "d="] or not er_tall(brukerinput[2:]):
    print("Ikke gyldig input")
    exit()

type_verdi, verdi = brukerinput.split("=")
verdi = float(verdi)

radius = omregning[type_verdi](verdi)

print(f"Radiusen er {radius:.1f}")
print(f"Arealet er {areal_sirkel(radius):.2f}")