import os
import time

snake = "~~~~~O"
for posisjon in range(30):
    os.system("cls")
    print(" " * posisjon + snake)
    print("----------------SNAKES--------------")
    snake = snake[::-1]
    print(" " * (30 - posisjon) + snake)
    snake = snake[::-1]
    time.sleep(0.3)
