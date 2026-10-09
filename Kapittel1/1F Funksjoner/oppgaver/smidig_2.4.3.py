def tell_vokaler(f_tekst):
    vokaler = "aeiouyæøå"
    return sum(1 for bokstav in f_tekst.lower() if bokstav in vokaler)

tekst = "Vil du være med på turen i høst?"
print(f"I teksten er det {tell_vokaler(tekst)} vokaler.")