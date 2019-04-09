"""
_author_ = " Harun Sefa DERE "
09.04.2019
"""
print("Hoşgeldin, eğer kendine güveniyorsan teste başla ve doğru olan cevabı yaz!")
print("Soruları yanlış cevaplamamaya dikkat ediniz çünkü her yanlış cevap -20 puandır!!!")
print("***********************************************************************************")
sorular = ["Bir yerin kuşbakışı görünümünün ölçeksiz ve kabataslak çizimine ne ad verilir?",\
            "Haritalarda kullanılan işaret ve sembollerin ne ifade ettiğini gösteren tabloya ne ad verilir?",\
            "Coğrafi olaylarin yayılış sahasını inceleyen ilkeye ne ilkesi denir?",\
            "Ekvator ve yakın çevresinin harita çizimlerinde hangi projeksiyon kullanılır?",\
            "Dünyayı çepecevre saran gaz ve buhar tabakasına ne denir?"]


cevaplar = ["A","B","C","B","D"]

cevap_A = ["Kroki" ,"Yol gösterici", "Bağlantı", "Konik", "Mezosfer"]
cevap_B = ["İzohips", "Lejant", "Yayılış", "Silindirik", "Ekzosfer"]
cevap_C = ["İzoterm", "Köşe tablosu", "Dağılış", "Düzlem", "İyonosfer"]
cevap_D = ["Tarama", "Hiçbiri", "Hiçbiri", "Hiçbiri", "Atmosfer"]

puan = 0
for i in range(len(sorular)):
    print("Soru "+str(i+1)+":"+sorular[i])
    print("A) " + cevap_A[i])
    print("B) " + cevap_B[i])
    print("C) " + cevap_C[i])
    print("D) " + cevap_D[i])
    cevap = input("Cevabınızı lüften buraya yazınız:")
    if(cevaplar[i] == cevap.upper()):
        print("Çok iyi,doğru bildiniz")
        print("Bir sonraki soruyu cevaplayınız!")
        puan +=1
        print("*************")
    else:
        print("Maalesef cevabınız yanlıştır!")
        print("Bir sonraki soruyu cevaplayınız")
        puan -=1
        print("*************")

#test sonu
print ("Testi bitirdiniz,bu testen aldiginiz puan: "+str(puan*20))

if puan <=0:
    print("Eksi puan aldınız lütfen testi inceleyiniz\nDaha çok çalışmalısınız ")
else:
    print("Başarılarınızın devamını dilerim...")