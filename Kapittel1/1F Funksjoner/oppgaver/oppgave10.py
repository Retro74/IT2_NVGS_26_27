from math import sqrt

def areal_trekant(a, b, c):
    if c>=a+b or a>=b+c or b>= a+c:
        print("Dette er ikke en reel trekant")
        exit()
    s = (a + b + c) / 2
    return sqrt(s * (s - a) * (s - b) * (s - c))
    

side1 = float(input("Skriv inn lengden på en av sidene i trekanten: "))
side2 = float(input("Skriv inn lengden på den neste av sidene i trekanten: "))
side3 = float(input("Skriv inn lengden på siste av sidene i trekanten: "))

print(f"Areal av denne trekanten er ca. {round(areal_trekant(side1,side2, side3),2)}")