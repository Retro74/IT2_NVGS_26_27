import matplotlib.pyplot as plt
import numpy as np
def f(x):
    return (1/2)*x**2+2*x-3

x = np.linspace(-10, 10, 101)
y = f(x)
funksjonsuttrykk = r"$f(x)=\frac{1}{2}x^2+2x-3$"
print(funksjonsuttrykk)
plt.plot(x, y, label=funksjonsuttrykk, color="darkgreen")
plt.axhline(0, color = "black", linewidth= 1)
plt.axvline(0, color = "black", linewidth= 1)
plt.grid()
plt.legend(fontsize=14)
plt.title(funksjonsuttrykk)
plt.show()