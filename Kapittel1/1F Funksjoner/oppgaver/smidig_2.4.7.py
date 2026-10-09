siffer = 4
def tall_med_siffer(f_siffer):
    if 0<=f_siffer<=9:
        return [x for x in range(0,100) if str(f_siffer) in str(x)]
    else:
        print("Sifferet må være mellom 0-9")
        return

print(tall_med_siffer(siffer))
