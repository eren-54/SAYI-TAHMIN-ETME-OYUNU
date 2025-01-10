# SAYI TAHMİN ETME OYUNU
import numpy as np
randomsayı = np.random.randint(0,50)
deneme =0
while deneme<5:
    hakkımız = 4-deneme
    deneme+=1
    tahmın = float(input("sayıyı tahmin et"))

    if tahmın < randomsayı:
        print(f"random sayı daha büyük ve kalan deneme hakkınız {hakkımız}")

    elif tahmın > randomsayı:
        print(f"random sayı daha küçük ve kalan deneme hakkınız {hakkımız}")
    elif tahmın==randomsayı:
        print(f"doğru tahmin ettiniz ve {deneme}.hakkınızda")
        break
if deneme ==5 :
    print(" üzgünüm hakkınız bitti")