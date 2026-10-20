def bits_til_ascii(bits):
    if len(bits) != 8:
        return "Feil: Må være 8 bit."
    return chr(int(bits, 2))

def ascii_til_bits(tegn):
    return f"{ord(tegn):08b}"

def signs_to_ascii(signs):
    binstring=""
    for sign in signs:
        binstring+= qam64_to_6bit[sign]
    #print(binstring)
    tekst = ""
    for i in range(0, len(binstring), 8):
        tekst+=bits_til_ascii(binstring[i:i+8])
    return tekst

##Lager ordboken bassert på listene av amp-verdier, faseverdier og 6 bits
amp_verdier = [x for x in range(1,9)]
fase_verdier = [x for x in range(0,360, int(360/8))]

bit_liste = []
for tall in range(64):
    bit_liste.append(f"{tall:06b}")

qam64_to_6bit = {}
for i in range(len(bit_liste)):
    qam64_to_6bit[(amp_verdier[i%len(amp_verdier)],fase_verdier[i//8] )]=bit_liste[i]

##Lager også den omvendte ordboken
bit6_to_qam64 = {bits:sign for sign,bits in qam64_to_6bit.items()}
##########################################

signs=[(6, 90), (7, 270), (6, 180), (7, 0), (3, 135), 
       (3, 90), (2, 0), (6, 180), (5, 135), (3, 180), 
       (2, 0), (1, 225), (2, 135), (7, 90), (2, 270), 
       (5, 270), (1, 45), (7, 0), (6, 225), (8, 225), 
       (4, 135), (7, 180), (6, 135), (6, 180)]

print(signs_to_ascii(signs))

signs_with_noise = [
    (3.13, 99.7), (7.02, 270.4), (5.91, 331.9), (4.83, 168.0),
    (1.81, 126.9), (6.86, 82.1), (5.69, 219.1), (6.85, 227.4),
    (1.76, 120.4), (6.76, 91.4), (5.91, 232.9), (4.24, 222.1),
    (1.68, 142.8), (8.2, 86.5), (1.13, 38.2), (2.33, 191.3)
]

def avrund_symbol(symbol):
    return (round(symbol[0]), round(symbol[1]/45)*45)

avrundet_signs = [avrund_symbol(sign) for sign in signs_with_noise]

print(signs_to_ascii(avrundet_signs))