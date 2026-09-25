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
#Endret en bokstav
mutert_endret_dna_sekvens = "GCCCTCCAGGACAGGCTGCATCAGAAGAGGCCATCAAGCAGGTCTGTTCCAAGGGCCTTTGCGTCAGGTGGGCTCAGGATTCCAGGGTGGCTGGACAGC"
#Fjernet en bokstav
mutert_fjernet_dna_sekvens = "GCCCTCCAGGACAGGTGCATCAGAAGAGGCCATCAAGCAGGTCTGTTCCAAGGGCCTTTGCGTCAGGTGGGCTCAGGATTCCAGGGTGGCTGGACAGCA"

rna_sekvens = "".join([dna_rna[syre] for syre in dna_sekvens])
mutert_endret_rna_sekvens = "".join([dna_rna[syre] for syre in mutert_endret_dna_sekvens])
mutert_fjernet_rna_sekvens = "".join([dna_rna[syre] for syre in mutert_fjernet_dna_sekvens])


print(f"a)  DNA-sekvens: {dna_sekvens}\ngir RNA-sekvens: {rna_sekvens}")

antall_aminosyrer = 0
print()
print(f"{'Orginal RNA':15}|{'Mutasjon 1':15}|{'Mutasjon 2':15}")
for i in range(0, len(rna_sekvens),3):
    aminosyre = kodontabell[rna_sekvens[i:i+3]]
#    if aminosyre == "Stop":
#        break
    antall_aminosyrer +=1
    print(f"{aminosyre:15}|"
          f"{kodontabell[mutert_endret_rna_sekvens[i:i+3]]:15}|"
          f"{kodontabell[mutert_fjernet_rna_sekvens[i:i+3]]:15}")

print(antall_aminosyrer)

#En bytte av bokstav vil bare gi en liten endring for akkurat denne aminosyren,
#Fjerning eller tillegg av bokstav vil endre hele sekvensen utover.