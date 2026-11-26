import numpy as np  # Matematisk bibliotek
import matplotlib.pyplot as plt

# Definerer funksjonen
x_list = np.linspace(-5, 5, 201)

def f_av_x(x,r):
    return np.sqrt(r**2-x**2)
radius=5

colors = ['#ff0000','#ffa500','#ffff00','#008000','#0000ff','#4b0082','#ae32ae']
plt.figure(figsize=(10,5))
for i in range(len(colors)):
    plt.plot(x_list,f_av_x(x_list,radius+(i/15)),linewidth=3, color=colors[i])  

plt.axis('off')
plt.show()