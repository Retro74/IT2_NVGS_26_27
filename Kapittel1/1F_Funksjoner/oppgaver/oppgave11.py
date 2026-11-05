from math import sqrt

def er_primtall(tall):
    if tall < 2:
        return False

    for divisor in range(2, int(sqrt(tall)) + 1):
        if tall % divisor == 0:
            return False

    return True

print(f"13 er {'' if er_primtall(13) else 'ikke'} et primtall")
print(f"123 er {'' if er_primtall(123) else 'ikke'} et primtall")
print(f"27 er {'' if er_primtall(27) else 'ikke'} et primtall")
print(f"61 er {'' if er_primtall(61) else 'ikke'} et primtall")