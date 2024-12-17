def ism_familiyani_almashtir(satr):
   
    qism = satr.split()  
    if len(qism) == 2:  
        ism, familiya = qism
        return f"{familiya} {ism}"  
    else:
        return "Xato: Satr ichida faqat ism va familiya bo'lishi kerak."

satr = "Ali Valiyev"
print(ism_familiyani_almashtir(satr)) 
