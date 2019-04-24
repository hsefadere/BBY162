metin = "Açık bilim, araştırma çıktılarına ve süreçlerine herkesin serbestçe erişmesini, bunların ortak kullanımını, dağıtımını ve üretimini kolaylaştıran bilim uygulamasıdır."

metinden = metin[:20]
print(metinden)

print("********************************************")
##################################################

liste = ["Açık Bilim", "Açık Erişim", "Açık Lisans", "Açık Eğitim", "Açık Veri", "Açık Kültür"]

for x in liste:
    print(x)

print("********************************************")
###################################################


sozluk = {"elma" : "Ağaçta yetişen bir tür meyve" , "salatalık" : "Fidan üzerinde büyüyen bir tür sebze" }

kelime= input("Aradığınız kelimeyi lütfen küçük harflerle buraya yazınız:")


while True:
    if kelime == "elma":
        print("Aradığınız kelime sözlükte bulunmaktadır")
        print(sozluk["elma"])
        break
    elif kelime == "salatalık":
        print("Aradığınız kelime sözlükte bulunmaktadır")
        print(sozluk["salatalık"])
        break
    else:
        print("Aradığınız kelime sözlükte bulunmamaktadır")
        break
