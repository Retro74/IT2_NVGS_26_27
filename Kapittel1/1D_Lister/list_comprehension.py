#alle_tall = [1,2,3,4,5,6,7,8,9,10]

#partall = []
#for tall in alle_tall:
#    if tall %2 == 0:
#        partall.append(tall)

#partall = [tall for tall in alle_tall if tall % 2 == 0]

#print(partall)

biler = [["Volvo", "XC90", 2019, 350_000],
         ["Kia", "Soul", 2020, 290_000],
         ["Saab", "9-5", 1992, 120_000],
         ["Tesla", "Model X", 2022, 510_000],
         ["Tesla", "Model Y", 2024, 450_000],
         ]

teslabiler = [tesla for tesla in biler if tesla[0]=="Tesla" and tesla[2]>=2023]
print(teslabiler)