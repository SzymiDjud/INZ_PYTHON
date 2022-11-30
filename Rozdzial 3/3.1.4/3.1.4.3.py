ogloszenie = {
    "title" : "",
    "description" : "",
    "category" : ["Sprzedaz", "Kupno", "Wynajem", "Oferta pracy", "Inne"],
    "create_date" : "",
    "author" : "",
    "phone_number" : "",
    "email" : "",
    "price" : 0,
    "views" : 0
}

def dzialaniaNaSlownikach(slownik):
    print(slownik)
    print("---------------------------Wypisz slownik---------------------------")
    print("")
    slownik["views"] = 100
    print(slownik)
    print("---------------------------Ustawienie wartosci pola 'views' na 100---------------------------")
    print("")
    slownik["nowe_pole"] = "nowe"
    print(slownik)
    print("---------------------------Dodanie nowego pola i zaincjalizowanie go wartoscia---------------------------")
    print("")
    slownik.update({"views":200, "price":50})
    print(slownik)
    print("---------------------------Aktualizacja wartosci pol w slowniku---------------------------")
    print("")
    slownik.pop("nowe_pole")
    print(slownik)
    print("---------------------------Usuniecie pola 'nowe_pole'---------------------------")
    print("")
    print(slownik.values())
    print("---------------------------Wypisanie wartosci---------------------------")
    print("")
    print(slownik.keys())
    print("---------------------------Wypisanie kluczy---------------------------")
    print("")
    print(slownik.items())
    print("---------------------------Wypisanie wszystkich elementow slownika---------------------------")
    print("")
    for klucz in slownik:
        print(klucz, '-', slownik[klucz])



dzialaniaNaSlownikach(ogloszenie)

