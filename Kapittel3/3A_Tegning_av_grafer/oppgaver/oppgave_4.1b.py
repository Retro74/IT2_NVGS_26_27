import numpy as np
import matplotlib.pyplot as plt

def fractionhandler(inputstring):
    """Tar imot en string med potensielt brøkstrek

    Args:
        inputstring (string): Tall eller en brøk med / 

    Returns: 2 verdier
        r-string: Formatert r-string med latex for brøk
        float: verdien av innsendt string i float
    """
    if not "/" in inputstring:
        return inputstring, float(inputstring)
    else:
        ##Brøk
        slash_pos = inputstring.index("/")
        inp_teller = inputstring[:slash_pos]
        inp_nevner = inputstring[slash_pos+1:]
        return fr"$\frac{{{inp_teller}}}{{{inp_nevner}}}$", float(inp_teller)/float(inp_nevner)

# Velg funksjonstype
grad = int(input("Velg grad på funksjonen (1, 2 eller 3): "))

# Definisjonsområde
x_min = float(input("Nedre grense for x: "))
x_max = float(input("Øvre grense for x: "))

# Genererer mange x-verdier
x = np.linspace(x_min, x_max, 500)

# Leser inn koeffisienter og beregner y
if grad == 1:
    a = input("Skriv inn a: ")
    r_string_a, a = fractionhandler(a)        
    b = input("Skriv inn b: ")
    r_string_b, b = fractionhandler(b)        
    y = a * x + b

    funksjonstekst = "f(x) = " + r_string_a + "x + " + r_string_b

elif grad == 2:
    a = input("Skriv inn a: ")
    r_string_a, a = fractionhandler(a)        
    b = input("Skriv inn b: ")
    r_string_b, b = fractionhandler(b)        
    c = input("Skriv inn c: ")
    r_string_c, c = fractionhandler(c)
    y = a * x**2 + b * x + c
    funksjonstekst = "f(x) = " + r_string_a + "x² + "+ r_string_b + "x + " + r_string_c

elif grad == 3:
    a = input("Skriv inn a: ")
    r_string_a, a = fractionhandler(a)        
    b = input("Skriv inn b: ")
    r_string_b, b = fractionhandler(b)        
    c = input("Skriv inn c: ")
    r_string_c, c = fractionhandler(c)
    d = input("Skriv inn d: ")
    r_string_d, d = fractionhandler(d)
    y = a * x**3 + b * x**2 + c * x + d
    funksjonstekst = "f(x) = " + r_string_a + "x³ + "+ r_string_b + "x² + " + r_string_c + "x + " + r_string_d

else:
    print("Ugyldig grad!")
    exit()

# Tegner grafen
plt.figure(figsize=(8, 5))

plt.plot(
    x,
    y,
    color="blue",
    linewidth=2,
    label=funksjonstekst
)

plt.axhline(0, color="black", linewidth=0.8)
plt.axvline(0, color="black", linewidth=0.8)

plt.title("Funksjonsgraf")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.grid()
plt.legend(fontsize=14)
plt.show()