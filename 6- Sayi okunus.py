# birler_basamagi = {
#     1 : "bir",
#     2 : "iki",
#     3 : "uc",
#     4 : "dort",
#     5 : "bes",
#     6 : "alti",
#     7 : "yedi",
#     8 : "sekiz",
#     9 : "dokuz",
#     0 : ""
#
# }
#
# onlar_basamagi = {
#     1 : "on",
#     2 : "yirmi",
#     3 : "otuz",
#     4 : "kirk",
#     5 : "elli",
#     6 : "atmis",
#     7 : "yetmis",
#     8 : "seksen",
#     9 : "doksan",
#     0 : ""
#
# }
#
#
# try:
#     while True:
#         sayi = input("2 basamakli bir sayi giriniz ! : ")
#
#         print("\n")
#
#         if len(sayi)!=2:
#             print("Lutfen en fazla 2 basamakli pozitif bir sayi giriniz ! \n")
#             continue
#
#         if int(sayi[0])<1:
#             print("Lutfen onlar basamagina en az 1 olacak sekilde rakam giriniz! Sayi 2 basamakli olmalidir\n\n")
#             continue
#
#         print(onlar_basamagi[int(sayi[0])]+birler_basamagi[int(sayi[1])])
#
# except ValueError:
#     print("Lutfen Rakam Giriniz ! ")
# finally:
#     print("Sonundaaaaa!!")
#

def sayiokunusu(sayi):

    birler_basamagi = {
        1: "bir",
        2: "iki",
        3: "uc",
        4: "dort",
        5: "bes",
        6: "alti",
        7: "yedi",
        8: "sekiz",
        9: "dokuz",
        0: ""

    }

    onlar_basamagi = {
        1: "on",
        2: "yirmi",
        3: "otuz",
        4: "kirk",
        5: "elli",
        6: "atmis",
        7: "yetmis",
        8: "seksen",
        9: "doksan",
        0: ""

    }


    return onlar_basamagi[int(sayi[0])]+birler_basamagi[int(sayi[1])]

while True:

    sayi = input("2 basamakli bir sayi giriniz ! : ")

    if len(sayi) != 2:
        print("Lutfen en fazla 2 basamakli pozitif bir sayi giriniz ! \n")

    if int(sayi[0]) < 1:
        print("Lutfen onlar basamagina en az 1 olacak sekilde rakam giriniz! Sayi 2 basamakli olmalidir\n\n")

print(sayiokunusu(sayi))






