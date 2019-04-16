"""
__author__= Harun Sefa DERE
13.04.2019
"""
#Adam asmaca oyunu
name=input("Lütfen isminizi giriniz:")
print("Adam asmaca oyununa hoşgeldin" ,name)
print("Konumuz renkler, hadi başlayalım")
#**************************#
import random
AdamAsmaca = ("☺☺☺☺☺","☺☺☺☺","☺☺☺","☺☺","☺",)
maxcan = len(AdamAsmaca) - 1
kelimeler = ("mavi","turuncu","sarı","siyah","beyaz","lacivert",
             "kırmızı","yeşil","mor","kahverengi","turkuaz","bej",
             "pembe","gri","bordo")
gizlikelime = random.choice(kelimeler)

tablo = "-" * len(gizlikelime)
hak = 0
havuz = []


while hak <= maxcan and tablo !=gizlikelime:
    print(AdamAsmaca[hak])
    print("Bu harfleri kullandın: ", havuz )
    print("Kelime: ", tablo)
    print("Kalan can: ", 5-hak)
    tahmin = input("\nHarf giriniz: ").lower()

    while tahmin in havuz:
        print("Bu harf zaten kullanıldı.")
        tahmin = input("\nHarf giriniz: ").lower()
    havuz.append(tahmin)
    if tahmin in gizlikelime:
        print("Güzel !!", tahmin, "harfi kelimede mevcut ")
        print("************************")
        yeni = ""
        for i in range(len(gizlikelime)):
            if tahmin == gizlikelime[i]:
                yeni += tahmin
            else:
                yeni += tablo[i]
        tablo = yeni
    else:
        print("Maalesef",tahmin," harfi kelimede mevcut değil !!!")
        print("************************")
        hak += 1
#adam asmaca sonu
if hak > maxcan:
    print("Kaybettinn :(")
    print("Cevap: ", gizlikelime)
else:
    print("Tebrikler!! Kazandın :)")
    print("Cevap: ", gizlikelime)
    
