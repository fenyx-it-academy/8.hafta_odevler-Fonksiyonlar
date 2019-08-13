def terssame():                                                 # fonksiyonumuzu adlandirdik
    kelime=list(input("Lutfen kelimenizi giriniz : "))          # kullanicidan veri aldik
    ters=list(reversed(kelime))                                 # verinin tersini bulduk

    if kelime == ters:                                          # veri ile ters verinin ayni olup olmadigini kotrol ettik ve sonucu verdik
        return True

    else:
        return False

print(terssame())                                               # fonksiyonumuzu cagirdik