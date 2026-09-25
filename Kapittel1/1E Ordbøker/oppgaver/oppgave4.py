import random 
dna_rna = {"A":"U",
           "T":"A",
           "C":"G",
           "G":"C",}

kodontabell = {  
  "UUU": "Fenylalanin", "CUU": "Leucin",       
  "AUU": "Isoleucin",   "GUU": "Valin",         
  "UUC": "Fenylalanin", "CUC": "Leucin",   
  "AUC": "Isoleucin",   "GUC": "Valin",        
  "UUA": "Leucin",      "CUA": "Leucin",        
  "AUA": "Metionin",    "GUA": "Valin",  
  "UUG": "Leucin",      "CUG": "Leucin",       
  "AUG": "Metionin",    "GUG": "Valin",         
  "UCU": "Serin",       "CCU": "Prolin",   
  "ACU": "Treonin",     "GCU": "Alanin",       
  "UCC": "Serin",       "CCC": "Prolin",        
  "ACC": "Treonin",     "GCC": "Alanin",  
  "UCA": "Serin",       "CCA": "Prolin", 
  "ACA": "Treonin",     "GCA": "Alanin",        
  "UCG": "Serin",       "CCG": "Prolin",   
  "ACG": "Treonin",     "GCG": "Alanin",       
  "UAU": "Tyrosin",     "CAU": "Histidin",      
  "AAU": "Asparagin",   "GAU": "Asparaginsyre",  
  "UAC": "Tyrosin",     "CAC": "Histidin",     
  "AAC": "Asparagin",   "GAC": "Asparaginsyre", 
  "UAA": "Stopp",       "CAA": "Glutamin", 
  "AAA": "Lysin",       "GAA": "Glutaminsyre", 
  "UAG": "Stopp",       "CAG": "Glutamin",      
  "AAG": "Lysin",       "GAG": "Glutaminsyre",  
  "UGU": "Cystein",     "CGU": "Arginin",      
  "AGU": "Serin",       "GGU": "Glycin",        
  "UGC": "Cystein",     "CGC": "Arginin",  
  "AGC": "Serin",       "GGC": "Glycin",       
  "UGA": "Stopp",       "CGA": "Arginin",       
  "AGA": "Arginin",     "GGA": "Glycin",  
  "UGG": "Tryptofan",   "CGG": "Arginin",     
  "AGG": "Arginin",     "GGG": "Glycin" 
}

dna_sekvens = "GCCCTCCAGGACAGGCTGCATCAGAAGAGGCCATCAAGCAGGTCTGTTCCAAGGGCCTTTGCGTCAGGTGGGCTCAGGATTCCAGGGTGGCTGGACAGC"
#Mutasjon 1: Endret en bokstav
nybokstav = random.choice(["A", "C", "G", "T"])
endrer_index = random.randint(0,int(len(dna_sekvens)/2)) #Endrer en i 1. halvdel
while nybokstav == dna_sekvens[endrer_index]:
    nybokstav = random.choice(["A", "C", "G", "T"])
print(f"Muterer ved å endre: {endrer_index+1} til {nybokstav}")
mutasjon1_dna_sekvens = dna_sekvens[0:endrer_index]+nybokstav + dna_sekvens[endrer_index+1::]
#Mutasjon 2: Fjernet en bokstav
print(f"Muterer ved å fjerne: {endrer_index+1} og legger til på slutten {nybokstav}")
mutasjon2_dna_sekvens = dna_sekvens[0:endrer_index]+dna_sekvens[endrer_index+1::]+nybokstav

rna_sekvens = "".join([dna_rna[syre] for syre in dna_sekvens])
mutasjon1_rna_sekvens = "".join([dna_rna[syre] for syre in mutasjon1_dna_sekvens])
mutasjon2_rna_sekvens = "".join([dna_rna[syre] for syre in mutasjon2_dna_sekvens])


print(f"a)  DNA-sekvens:  {dna_sekvens}\n"
      f"gir RNA-sekvens:  {rna_sekvens}\n"
      f"Mutert DNA1 sekv: {mutasjon1_dna_sekvens}"
      f"Mutert RNA1 sekv: {mutasjon1_rna_sekvens}\n"
      f"Mutert DNA2 sekv: {mutasjon2_dna_sekvens}"
      f"Mutert RNA2 sekv: {mutasjon2_rna_sekvens}")

antall_aminosyrer = 0
print()
print(f'{"-"*15}+{"-"*15}+{"-"*15}+{"-"*15}')
print(f"{'Triplet':15}|{'Orginal RNA':15}|{'Mutasjon 1':15}|{'Mutasjon 2':15}")
print(f'{"-"*15}+{"-"*15}+{"-"*15}+{"-"*15}')

for i in range(0, len(rna_sekvens),3):
    aminosyre = kodontabell[rna_sekvens[i:i+3]]
#    if aminosyre == "Stop":
#        break
    antall_aminosyrer +=1
    print(f"{'('+ str(i+1) + '-' + str(i+3) + ')':15}|"
          f"{aminosyre:15}|"
          f"{kodontabell[mutasjon1_rna_sekvens[i:i+3]]:15}|"
          f"{kodontabell[mutasjon2_rna_sekvens[i:i+3]]:15}")

print(f'{"-"*15}+{"-"*15}+{"-"*15}+{"-"*15}')

print(antall_aminosyrer)

#En bytte av bokstav vil bare gi en liten endring for akkurat denne aminosyren,
#Fjerning eller tillegg av bokstav vil endre hele sekvensen utover.