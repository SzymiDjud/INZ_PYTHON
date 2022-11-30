title = ""
description = ""
category = ("Sprzedaz", "Kupno","Wynajem", "Oferta pracy", "Inne" )
create_date = ""
author = ""
phone_number = ""
email = ""
price = 0
views = 0


def wpiszDane():

    global title, description, category, author, phone_number, email, price, views
    title = input("Wpisz tytul ogloszenia: ")
    description = input("Wpisz opis ogloszenia: ")
    category = input("Wpisz kategorie ogloszenia: ")
    author = input("Wpisz autora ogloszenia: ")
    phone_number = input("Wpisz numer telefonu autora ogloszenia: ")
    email = input("Wpisz email kontakowy autora ogloszenia: ")

    price = float((input("Wpisz cene: ")))
    views = int((input("Wpisz liczbe wyswietlen ogloszenia: ")))

wpiszDane()
with open('ogloszenie2.txt','w') as f:
    f.write(title+description)