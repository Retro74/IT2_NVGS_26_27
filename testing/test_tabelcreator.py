import tableCreator as tc
tabell = [
    ["Land","Norge", "Sverige", "Dannmark", "Finland"],
    ["Hovedstad", "Oslo", "Stockholm", "Kjøbenhavn", "Helsinki"],
    ["Pengeenhet","NOK", "SEK", "DK", "Mark"],
    ["Innbyggere", 6.1, 12.0, 7.2, 4.9]]

print(tc.create_table(tabell, True))
