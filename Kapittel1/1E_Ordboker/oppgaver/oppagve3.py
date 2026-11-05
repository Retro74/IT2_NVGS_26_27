personer = {
  "Sophie": 18, "Noah": 18, "Olivia": 29, "Oscar": 21,
  "Oliver": 25, "Sofia": 27, "Ella": 23, "Leah": 21,
  "Lucas": 23, "Maya": 25, "Isaac": 29, "Axel": 27, 
  "Frida": 23, "Emil": 26, "Emma": 23, "Ingrid": 18,
  "Phillip": 25, "Jacob": 24, "Nora": 21, "William": 22
}

print(f'a) {set(personer.values())}')

unikealdre = {alder:navn for navn,alder in personer.items()}
print(f'b) {unikealdre}')

alder_personer = {}
for navn, alder in personer.items():
    if alder_personer.get(alder):
        alder_personer[alder].append(navn)
    else:
        alder_personer[alder] = [navn]

print(f"c) {alder_personer}")
