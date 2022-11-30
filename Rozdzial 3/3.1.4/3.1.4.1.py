title = ""
description = ""
category = ["Sprzedaz", "Kupno","Wynajem", "Oferta pracy", "Inne" ]
create_date = ""
author = ""
phone_number = ""
email = ""
price = 0
views = 0

def listy(lista):
    print(lista[0])
    print("---------------------------Pierwszy element listy---------------------------")
    print(lista[-1])
    print("---------------------------Ostatni element listy---------------------------")
    lista.append("Nowa kategoria")
    print(lista)
    print("---------------------------Nowy element listy---------------------------")
    lista.insert(1,"Nowa kategoria")
    drugalista = ["Auto", "Dom"]
    lista.extend(drugalista)
    print(lista)
    print("---------------------------Rozszerzenie listy o druga8---------------------------")
    sumaList = lista + drugalista
    print(sumaList)
    print("---------------------------Dodawanie krotek---------------------------")
    lista[0] = "Brak kategorii"
    print(lista)
    print("---------------------------Zmiana elementu w krotce---------------------------")
    print(lista.reverse())
    print("---------------------------Odwrócenie kolejnosci---------------------------")
    print(lista.sort())
    print("---------------------------Sortowanie listy---------------------------")
    print(lista.count("Kupno"))
    print("---------------------------Zlicz ilość wystapień 'Kupno'---------------------------")
    print(lista.index("Wynajem"))
    print("---------------------------Wypisz index 'Wynajem'---------------------------")
    print("Wynajem" in lista)
    print("---------------------------Sprawdzenie czy element znajduje się w liście---------------------------")
    lista.pop()
    print(lista)
    print("---------------------------Usuniecie ostatniego elementu---------------------------")
    print(len(lista))
    print("---------------------------Dlugosc listy---------------------------")

listy(category)