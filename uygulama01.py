"""
_author_ = "harun sefa dere"
"""
print("Hoşgeldin,eğer kendine güveniyorsan teste başla ve dogru olan cevabı yaz!")
print("Soruları yanlış cevaplamamaya dikkat ediniz çünkü her yanlış cevap -20 puandır!!!")

puan = 0
cevaplar = ["A","B","C","B","D"]

#soru 1
soru1 = "1-Bir yerin kuşbakışı görünümünün ölçeksiz ve kabataslak çizimine ne ad verilir?\nA)Kroki   B)İzohips   C)İzoterm   D)Tarama          buraya yazınız lüften:"
cevap = input(soru1)
if cevaplar[0] == cevap.upper():
    print("Çok iyi,doğru bildiniz")
    print("Bir sonraki soruyu cevaplayınız!")
    puan +=1
else:
    print("Maalesef cevabınız yanlıştır!")
    print("Bir sonraki soruyu cevaplayınız")
    puan -=1

#soru 2
soru2="2-Haritalarda kullanılan işaret ve sembollerin ne ifade ettiğini gösteren tabloya ne ad verilir?\nA)Yol gösterici   B)Lejant   C)Köşe tablosu  D)Hiçbiri          buraya yazınız lüften:"
cevap =input(soru2)
if cevaplar[1] == cevap.upper():
    print("Çok iyi,doğru bildiniz")
    print("Bir sonraki soruyu cevaplayınız")
    puan += 1
else:
    print("Maalesef cevabınız yanlıştır")
    print("Bir sonraki soruyu cevaplayınız")
    puan -= 1

#soru 3
soru3="3-Coğrafi olaylarin yayılış sahasını inceleyen ilkeye ne ilkesi denir?\nA)Bağlantı   B)Yayılış   C)Dağılış   D)Hiçbiri          buraya yazınız lüften:"
cevap =input(soru3)
if cevaplar[2] == cevap.upper():
    print("Çok iyi,doğru bildiniz")
    print("Bir sonraki soruyu cevaplayınız!")
    puan +=1
else:
    print("Maalesef cevabınız yanlıştır!")
    print("Bir sonraki soruyu cevaplayınız")
    puan -=1

#soru 4
soru4="4-Ekvator ve yakın çevresinin harita çizimlerinde hangi projeksiyon kullanılır?\nA)Konik   B)Silindirik   C)Düzlem   D)Hiçbiri          buraya yazınız lüften:"
cevap =input(soru4)
if cevaplar[3] == cevap.upper():
    print("Çok iyi,dogru bildiniz")
    print("Bir sonraki soruyu cevaplayınız!")
    puan +=1
else:
    print("Maalesef cevabınız yanlıştır!")
    print("Bir sonraki soruyu cevaplayınız")
    puan -=1

#soru 5
soru5="5-Dünyayı çepecevre saran gaz ve buhar tabakasına ne denir?\nA)Mezosfer   B)Ekzosfer   C)İyonosfer   D)Atmosfer          buraya yazınız lüften:"
cevap =input(soru5)
if cevaplar[4] == cevap.upper():
    print("Çok iyi,doğru bildiniz")
    print("Bir sonraki soruyu cevaplayınız!")
    puan +=1
else:
    print("Maalesef cevabınız yanlıştır!")
    print("Bir sonraki soruyu cevaplayınız")
    puan -=1

#test sonu
print ("Testi bitirdiniz,bu testen aldiginiz puan: "+str(puan*20))
print ("Düşük puan aldıysanız daha çok çalışmalısınız...\nBaşarılarınızın devamını dilerim")