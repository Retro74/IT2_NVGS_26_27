def tell_vokaler(f_tekst):
    vokaler = "aeiouyæøå"
    ant_vokaler =0
    for bokstav in f_tekst:
        if bokstav.lower() in vokaler:
            ant_vokaler+=1
    return ant_vokaler

tekst = "Vil du være med på turen i høst?"
print(f"I teksten er det {tell_vokaler(tekst)} vokaler.")