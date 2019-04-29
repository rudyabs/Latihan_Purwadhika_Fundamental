
angka_1 = int(input("Masukan angka ke-1: "))
angka_2 = int(input("Masukan angka ke-2: "))

pemb_1 = 1
pemb_2 = 1
faktorial_1 = set()
faktorial_2 = set()
kelipatan_1 = set()
kelipatan_2 = set()
bilangan_1 = angka_1
bilangan_2 = angka_2

# FPB

# Melihat faktor dari bilangan
while pemb_1 <= angka_1:
    if angka_1 % pemb_1 == 0:
        faktorial_1.add(pemb_1)
        pemb_1 += 1  
    elif angka_1 % pemb_1 > 0:
        pemb_1 += 1
        continue
    else: 
        break

while pemb_2 <= angka_2:
    if angka_2 % pemb_2 == 0:
        faktorial_2.add(pemb_2)
        pemb_2 += 1
    elif angka_2 % pemb_2 > 0:
        pemb_2 += 1
        continue
    else:
        break

# tes hasil loop
# print(faktorial_1)
# print(faktorial_2)
# print(faktorial_1.intersection(faktorial_2))

fpb = faktorial_1.intersection(faktorial_2)
print("FPB dari {} dan {} adalah =".format(angka_1, angka_2), max(fpb))

# KPK
# print(faktorial_1.issubset(faktorial_2))

while kelipatan_1.isdisjoint(kelipatan_2) == True:
    kelipatan_1.add(bilangan_1)
    kelipatan_2.add(bilangan_2)
    bilangan_1 += angka_1
    bilangan_2 += angka_2
 
# print(kelipatan_1)
# print(kelipatan_2)

kpk = kelipatan_1.intersection(kelipatan_2)
print("KPK dari {} dan {} adalah =".format(angka_1, angka_2), min(kpk))

