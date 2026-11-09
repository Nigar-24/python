telebeler = []
while True:
    print("\n--- Tələbə Jurnalı ---")
    print("1. Tələbə əlavə et")
    print("2. Jurnalı göstər")
    print("3. Çıxış")
    secim = input("Seçiminiz (1, 2, 3): ")
    if secim == "1":
        ad = input("Tələbənin adı: ")
        qiymet = input("Qiyməti: ")
        telebeler.append((ad, qiymet))
        print("Tələbə əlavə olundu!")
    elif secim == "2":
        print("\n--- Jurnalın siyahısı ---")
        if len(telebeler) == 0:
            print("Jurnal boşdur.")
        else:
            for item in telebeler:
                print("Ad:", item[0], "| Qiymət:", item[1])       
    elif secim == "3":
        print("Proqramdan çıxılır")
        break
    else:
        print("Yanlış seçim etdiniz! yenidən yoxlayın.")
