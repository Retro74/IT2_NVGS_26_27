def fakultet(tall, grense):
    
    if grense == tall:
        return tall
    else:
        return tall * fakultet(tall+1, grense)


print(f"5! = {fakultet(1,5)}")