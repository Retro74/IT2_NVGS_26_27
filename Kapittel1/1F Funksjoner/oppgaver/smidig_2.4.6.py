def harm_gjsnitt(f_liste):    
    nevner = 0
    for tall in f_liste:
        nevner += 1/tall
    if nevner == 0:
        print("Ikke liste")
        return
    return len(f_liste)/nevner

lst= [50,100]
print(f"Det harmoniske gjennomsnittet er {harm_gjsnitt(lst):.1f}")

