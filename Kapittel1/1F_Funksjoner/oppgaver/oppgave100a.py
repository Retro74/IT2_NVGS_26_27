def skrivUtTallUnder(tall, grense):
    
    if grense == tall:
        print(tall)
    else:
        print(tall)
        skrivUtTallUnder(tall+1, grense)


skrivUtTallUnder(1, 10)