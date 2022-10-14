import random
import time

rastgelesayi = random.randint(1,50)

hak = 7

print("******SAYI TAHMİN OYUNU******")
time.sleep(2)

while True:
	tahminsayi = int(input("Lütfen 1 ile 50 arrasında bir sayı seç. "))
	print("Doğrulanılıyor...")
	time.sleep(1)	
	hak -=1
	
	if hak== 0:
		print("Hakkın Doldu Sayı ",rastgelesayi,"idi")
	elif tahminsayi > rastgelesayi:
		print("Tahmin ettiğin sayı büyük kalan hakkın ",hak)		
	elif tahminsayi < rastgelesayi:
		print("Tahmin ettiğin sayı küçük kalan hakkın ",hak)
	else:
		print("Tebrikler Oyunu Kazandınız")
		
	