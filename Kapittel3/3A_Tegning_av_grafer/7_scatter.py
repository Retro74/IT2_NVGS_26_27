import matplotlib.pyplot as plt
import random as rnd

ant_obs = 15

x_pos= [rnd.randint(1,20) for _ in range(ant_obs)]
y_pos= [rnd.randint(50,120) for _ in range(ant_obs)]
sizes = [rnd.randint(5,300) for _ in range(ant_obs)]
farger = plt.cm.viridis([i/14 for i in range(15)])#
plt.scatter(x_pos, y_pos, s=sizes, c=farger, label="MyDots")

#x_pos= [rnd.randint(1,20) for _ in range(ant_obs)]
#y_pos= [rnd.randint(50,120) for _ in range(ant_obs)]
#sizes = [rnd.randint(5,300) for _ in range(ant_obs)]
#plt.scatter(x_pos, y_pos, s=sizes, color="blue", label="Høyre")

plt.legend()
plt.title("Tilfeldige verdier")
plt.show()