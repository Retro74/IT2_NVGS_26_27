def beregninger(f_a,f_b):
    return f_a+f_b, f_a-f_b if a>b else f_b-f_a, f_a*f_b,f_a/f_b 
a, b = 2, 3
sum_ab, diff_ab, prod_ab, kvot_ab = beregninger(a,b)

print(f"Tallene brukt i bergningene er {a} og {b}")
print(f"Summen av {a} og {b} er {sum_ab}")
print(f"Forskjellen mellom  {a} og {b} er {diff_ab}")
print(f"Produktet av {a} og {b} er {prod_ab}")
print(f"Kvotienten av {a} og {b} er {kvot_ab}")

