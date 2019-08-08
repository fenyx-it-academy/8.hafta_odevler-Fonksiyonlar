def read_number():
    """En fazla dort haneye kadar girilen sayilarin okunusunu yazdiran fonksiyon """

    num_dict = {1:"bir", 2:"iki", 3:"üç", 4:"dort", 5:"bes", 6:"alti", 7:"yedi",
                8:"sekiz", 9:"dokuz", 10:"on", 20:"yirmi", 30:"otuz", 40:"kirk",
                50:"elli", 60:"atmis", 70:"yetmis", 80:"seksen", 90:"doksan",
                100:"yuz", 1000:"bin"}                                          # Sayilarin yazilaslari icin kume tanimlanir

    sayi = input("Lutfen En fazla Dort haneli bir sayi giriniz :")              # yazdirilacak sayi girisi alinir
    yazi=[]                                                                     # bos liste olusturulur
    sayac=0                                                                     # girilen sayinin hangi basamakta oldugunu tespit icin sayac olusturulur
    for i in sayi[::-1]:                                                        # girilen sayiyinin her rakamini string olarak donduren dongu baslatilir

        ara_deger = int(i)*(10**sayac)                                          # sayac yardimi ile dongudeki sayinin ondalik karsiligi degiskene atanir

        if ara_deger in num_dict:                                               # bu deger sozlukte varsa
            yazi+=[num_dict[ara_deger]]                                         # yazi listesine degerini ekle
            sayac += 1                                                          # sayaci bir arttir
        elif ara_deger==0:                                                      # eger sayi 0 ise ara deger 0 olur. ozaman sayaci arttirip devam eder.
            sayac += 1
        else:                                                                   # bunlardan biri degilse orn: 900
            yazi+=[num_dict[int(i)]+num_dict[10**sayac]]                        # o zaman dokuz degerinin sozlukteki karsiligi ile yuzler basamaginin sozlukteki karsiligini bulup yan yana ekler dokuz + yuz gibi
            sayac+=1

    yazi = reversed(yazi)                                                       # listeye eklenen yazilari tersine cevir
    print(*yazi)                                                                # listenin degerlerini ekrana bastir

read_number()



