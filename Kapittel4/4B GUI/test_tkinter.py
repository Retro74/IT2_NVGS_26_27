import tkinter as tk

def si_hei():
    etikett.config(text="Hei, " + felt.get() + "!")

vindu = tk.Tk()
vindu.title("Enkel GUI")
vindu.geometry("300x150")

tk.Label(vindu, text="Skriv navnet ditt:").pack(pady=5)

felt = tk.Entry(vindu)
felt.pack(pady=5)

tk.Button(vindu, text="Si hei", command=si_hei).pack(pady=5)

etikett = tk.Label(vindu, text="")
etikett.pack(pady=5)

vindu.mainloop()