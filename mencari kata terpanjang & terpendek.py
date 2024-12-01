def cari_kata_terpendek_terpanjang(teks):
    kata_kata = teks.split()
    
    kata_terpendek = min(kata_kata, key=len)
    kata_terpanjang = max(kata_kata, key=len)
    
    return kata_terpendek, kata_terpanjang

teks_input = input("Masukkan kalimat: ")

kata_terpendek, kata_terpanjang = cari_kata_terpendek_terpanjang(teks_input)

print(f"Kata terpendek: '{kata_terpendek}', Kata terpanjang: '{kata_terpanjang}'")