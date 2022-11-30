title = ""
description = ""
category = ("Sprzedaz", "Kupno","Wynajem", "Oferta pracy", "Inne" )
create_date = ""
author = ""
phone_number = ""
email = ""
price = 0
views = 0

def krotki(krotka):
    print(krotka[0])
    print("---------------------------Pierwszy element krotki---------------------------")
    print(krotka[-1])
    print("---------------------------Ostatni element krotki---------------------------")
    krotka.append("Nowa kategoria")
    print(krotka)
    print("---------------------------Nowy element krotki---------------------------")
    krotka.insert(1,"Nowa kategoria")
    drugakrotka = ("Auto", "Dom")
    krotka.extend(drugakrotka)
    print(krotka)
    print("---------------------------Rozszerzenie krotki o druga8---------------------------")
    sumaKrotek = krotka + drugakrotka
    print(sumaKrotek)
    print("---------------------------Dodawanie krotek---------------------------")
    krotka[0] = "Brak kategorii"
    print(krotka)
    print("---------------------------Zmiana elementu w krotce---------------------------")
    print(krotka.reverse())
    print("---------------------------Odwrócenie kolejnosci---------------------------")
    print(krotka.sort())
    print("---------------------------Sortowanie krotki---------------------------")
    print(krotka.count("Kupno"))
    print("---------------------------Zlicz ilość wystapień 'Kupno'---------------------------")
    print(krotka.index("Wynajem"))
    print("---------------------------Wypisz index 'Wynajem'---------------------------")
    print("Wynajem" in krotka)
    print("---------------------------Rozszerzenie krotki o druga---------------------------")
    krotka.pop()
    print(krotka)
    print("---------------------------Usuniecie ostatniego elementu---------------------------")
    print(len(krotka))
    print("---------------------------Dlugosc krotki---------------------------")



krotki(category)