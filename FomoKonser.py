def konser(Tiket, Lokasi, TotalWaktu: int):
    #MENYIMPAN TIPE HARGA TIKET YANG DIPILIH
    harga_tiket = {
        'Tiket A': 350_000,
        'Tiket B': 270_000,
        'Tiket C': 150_000
    }

    #MENYIMPAN LOKASI KONSER DAN BIAYA TRANSPORTASI
    biaya_transportasi = {
        'Jakarta': 400_000,
        'Surabaya': 360_000,
        'Bandung': 390_000,
        'Yogyakarta': 0
    }

    #MENYIMPAN BIAYA PENGINAPAN BERDASARKAN LOKASI PER HARI
    biaya_penginapan_perhari = {
        'Jakarta': 250_000,
        'Surabaya': 220_000,
        'Bandung': 200_000,
        'Yogyakarta': 0
    }

    #MENYIMPAN BIAYA TAMBAHAN PENGINAPAN PER JAM
    biaya_tambahan_perjam = {
        'Jakarta': 40_000,
        'Surabaya': 35_000,
        'Bandung': 30_000,
        'Yogyakarta': 0
    }

    if TotalWaktu < 24:
        return (harga_tiket[Tiket] + (biaya_transportasi[Lokasi] * 2) + (biaya_tambahan_perjam[Lokasi] * TotalWaktu))

    elif (TotalWaktu == 24):
        return (harga_tiket[Tiket] + (biaya_transportasi[Lokasi] * 2) + biaya_penginapan_perhari[Lokasi])
    else:
        return (harga_tiket[Tiket] + (biaya_transportasi[Lokasi] * 2) + biaya_penginapan_perhari[Lokasi] + (biaya_tambahan_perjam[Lokasi] * (TotalWaktu-24)))
    #fungsi ini mengembalikan Total Biaya