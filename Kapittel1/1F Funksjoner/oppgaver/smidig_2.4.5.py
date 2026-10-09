def pyramide(size):
    sizes = {"s":3,
             "m":5,
             "l":7}
    if not sizes.get(size):
        print("Uriktig størrelse valgt")
        return
    for i in range(1,sizes[size]+1):
        print((sizes[size]- i)*" " + "*"*((i*2)-1))
print("Liten pyramide:")
pyramide("s")
print("Medium pyramide:")
pyramide("m")
print("Stor pyramide:")
pyramide("l")