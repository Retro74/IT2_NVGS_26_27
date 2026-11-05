def fibonatch(tall1, tall2, antall, grense):
    
    if grense == antall:
        return tall1 + tall2
    else:
        return str(tall1+tall2) + ", " + str(fibonatch(tall2, tall1+tall2, antall+1, grense))



print(f"20 første fibonatccitallen er: 1, 1, " + fibonatch(1,1,3,20))