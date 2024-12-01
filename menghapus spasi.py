def hapus_spasi_ganda(teks):
    return ' '.join(teks.split())

teks_input = input("Masukkan teks: ")

teks_output = hapus_spasi_ganda(teks_input)

print(f"Teks setelah menghapus spasi ganda: '{teks_output}'")