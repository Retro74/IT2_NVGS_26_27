import numpy as np
import matplotlib.pyplot as plt

# Velg funksjonstype
grad = int(input("Velg grad på funksjonen (1, 2 eller 3): "))

# Definisjonsområde
x_min = float(input("Nedre grense for x: "))
x_max = float(input("Øvre grense for x: "))

# Genererer mange x-verdier
x = np.linspace(x_min, x_max, 500)

# Leser inn koeffisienter og beregner y
if grad == 1:
    a = float(input("Skriv inn a: "))
    b = float(input("Skriv inn b: "))

    y = a * x + b
    funksjonstekst = f"f(x) = {a}x + {b}"

elif grad == 2:
    a = float(input("Skriv inn a: "))
    b = float(input("Skriv inn b: "))
    c = float(input("Skriv inn c: "))

    y = a * x**2 + b * x + c
    funksjonstekst = f"f(x) = {a}x² + {b}x + {c}"

elif grad == 3:
    a = float(input("Skriv inn a: "))
    b = float(input("Skriv inn b: "))
    c = float(input("Skriv inn c: "))
    d = float(input("Skriv inn d: "))

    y = a * x**3 + b * x**2 + c * x + d
    funksjonstekst = f"f(x) = {a}x³ + {b}x² + {c}x + {d}"

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
plt.legend()

plt.show()