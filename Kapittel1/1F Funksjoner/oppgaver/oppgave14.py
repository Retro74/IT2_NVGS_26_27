import statistics

def analyser_liste(tall_liste):

    sortert = sorted(tall_liste)

    resultat = {
        "Gjennomsnitt": statistics.mean(tall_liste),
        "Standardavvik": statistics.stdev(tall_liste),
        "Median": statistics.median(tall_liste),
        "Q1": statistics.median(sortert[:len(sortert)//2]),
        "Q3": statistics.median(sortert[(len(sortert)+1)//2:]),
        "Typetall": statistics.mode(tall_liste),
        "Maks": max(tall_liste),
        "Min": min(tall_liste)
    }

    resultat["Kvartilbredde"] = resultat["Q3"] - resultat["Q1"]
    resultat["Variasjonsbredde"] = resultat["Maks"] - resultat["Min"]

    return resultat

tall = [2, 4, 5, 5, 6, 7, 8, 10, 12, 15]

analyse = analyser_liste(tall)

for nøkkel, verdi in analyse.items():
    print(f"{nøkkel}: {verdi}")