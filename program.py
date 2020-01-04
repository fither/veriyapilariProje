import os, sys
import PyPDF2
import docx2txt
from difflib import SequenceMatcher

def arama(kelime1, kelime2):
	return SequenceMatcher(None, kelime1, kelime2).ratio()

yol = "./"
aranacak_kelime = "mesela"
esik_degeri = 0.7

aranacak_kelime = raw_input("aranacak kelimeyi giriniz: ")

for file in os.listdir(yol):
	if file.endswith(".txt"):
		cnt=1
		print(str(file) + " txt dosyasi aciliyor")
		# with open(file, "r+",encoding = "utf-8") as f:
		with open(file, "r+") as f:
			for line in f:
				for word in line.split():
					eslesme_orani = arama(aranacak_kelime, word)
					if eslesme_orani > esik_degeri:
						print(aranacak_kelime + " " + str(file) + " dosyasinda bulundu")
						print("\teslesme orani -> " + str(eslesme_orani))
						print("eslesilen satir -> " + str(cnt))
				cnt+=1

	if file.endswith(".html"):
		print(str(file) + " html dosyasi aciliyor")
		# with open(file, "r+",encoding = "utf-8") as f:
		with open(file, "r+") as f:
			cnt=1
			for line in f:
				for word in line.split():
					# print(word)
					eslesme_orani = arama(aranacak_kelime, word)
					if eslesme_orani > esik_degeri:
						print(aranacak_kelime + " " + str(file) + " dosyasinda bulundu")
						print("\teslesme orani -> " + str(eslesme_orani))
						print("eslesilen satir -> " + str(cnt))
				cnt+=1

	elif file.endswith(".pdf"):
		print( str(file) + " pdf dosyasi aciliyor")
		cnt=1

		for i in range(PyPDF2.PdfFileReader(open(file, "rb"), strict=False).getNumPages()):
			sayfa = PyPDF2.PdfFileReader(open(file, "rb"), strict=False).getPage(i).extractText()

		parcali = sayfa.split(" ")
		kelimeli = []
		for kelime in parcali:
			kelime=kelime.replace("\n","")
			kelimeli.append(kelime)
		for i in range(len(kelimeli)):
			if kelimeli[i] != "":
				word = kelimeli[i]
				# print(word)
				eslesme_orani = arama(aranacak_kelime, word)
				if eslesme_orani > esik_degeri:
					print(aranacak_kelime + " " + str(file) + " dosyasinda bulundu")
					print("\teslesme orani -> " + str(eslesme_orani))

	elif file.endswith(".docx"):
		print(str(file) + " docx dosyasi aciliyor")
		text = docx2txt.process(file)
		for word in text.split():
			# print(word)
			eslesme_orani = arama(aranacak_kelime, word)
			if eslesme_orani > esik_degeri:
				print(aranacak_kelime + " " + str(file) + " dosyasinda bulundu")	
				print("\teslesme orani -> " + str(eslesme_orani))