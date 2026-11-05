def tell_antall_unike_bokstvaver(f_tekst):
    unikebokstaver = set()
    for bokstav in f_tekst:
        if bokstav.isalpha():
            unikebokstaver.add(bokstav.lower())
    return len(unikebokstaver)

tekst = "Sesam sesam lukk deg opp!"
print(f"Det er {tell_antall_unike_bokstvaver(tekst)} unike bokstaver i teksten")