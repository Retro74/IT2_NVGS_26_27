import matplotlib.pyplot as plt
import random as rnd

ant_obs = 15

x_pos= [rnd.randint(0,400) for _ in range(ant_obs)]
y_pos= [rnd.randint(0,400) for _ in range(ant_obs)]
sizes = [rnd.randint(100,1000) for _ in range(ant_obs)]
#farger = plt.cm.viridis([i/14 for i in range(ant_obs)])#
farger = [f"#{rnd.randint(0, 0xFFFFFF):06X}" for _ in range(ant_obs)]
plt.scatter(x_pos, y_pos, s=sizes, c=farger, label="MyDots")

plt.title("Tilfeldige verdier")
plt.show()