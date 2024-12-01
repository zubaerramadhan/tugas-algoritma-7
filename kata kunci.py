def hitung_kemunculan(teks, kata_kunci):
    return teks.lower().count(kata_kunci.lower())

teks_berita = input("Masukkan teks berita: ")
kata_kunci = input("Masukkan kata kunci yang ingin dicari: ")

jumlah_kemunculan = hitung_kemunculan(teks_berita, kata_kunci)

print(f"Kata '{kata_kunci}' muncul sebanyak {jumlah_kemunculan} kali dalam teks berita.")