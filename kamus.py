meme_dict = {
            "CRINGE": "Sesuatu yang sangat aneh atau memalukan",
            "LOL": "Tanggapan umum terhadap sesuatu yang lucu",
            "CMIIW": "digunakan saat seseorang tidak terlalu yakin 100 persen bahwa yang dikatakannya adalah benar",
            "TBH": "mengekspresikan kejujuran seseorang",
            "IMO": "ungkapan yang digunakan saat kita akan menyatakan pendapat",
            "OOT": "digunakan saat seseorang sedang membahas sebuah topik, namun di saat bersamaan dia menceletukkan sebuah topik yang berbeda, yang tidak ada kaitannya",
            }

word = input("Ketik kata yang tidak Kamu mengerti (gunakan huruf kapital semua!): ")

if word in meme_dict.keys():
    print('ARTINYA: ')
    print(meme_dict[word])
else:
    print('MAAF KATA BELUM TERSEDIA/BELUM DI UPDATE')
