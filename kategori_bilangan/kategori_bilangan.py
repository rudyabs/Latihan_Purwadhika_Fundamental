# KATEGORI BILANGAN
bilangan_input = int(input("Masukan angka ="))
kategori = []

# bilangan bulat
if bilangan_input * 1 == bilangan_input:
    kategori.append("bulat")

# bilangan cacah
if bilangan_input >= 0:
    kategori.append("cacah")

# bilangan negatif
if bilangan_input < 0:
    kategori.append("negatif")

# bilangan nol
if bilangan_input * 1 == 0:
    kategori.append("nol")

# bilangan asli
if bilangan_input > 0 : 
    kategori.append("asli")

# bilangan ganjil
if bilangan_input % 2 > 0 and bilangan_input != 0:
    kategori.append("ganjil")

# bilangan genap
if bilangan_input % 2 == 0 and bilangan_input != 0:
    kategori.append("genap")

# bilangan prima
if bilangan_input > 1 and bilangan_input != 4:
    if bilangan_input == 2 or 3:
        kategori.append("prima")
    elif (bilangan_input + 6) / 5 != 0:
        kategori.append("prima") 

# bilangan komposit
if bilangan_input > 2 and bilangan_input / 1 == bilangan_input and bilangan_input / bilangan_input == 1:
    if bilangan_input % 2 == 0 or bilangan_input % 3 == 0:
        kategori.append("komposit")

# output kategori bilangan`
print(kategori)


 
