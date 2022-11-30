title = ""
description = ""
category = ("Sprzedaz", "Kupno","Wynajem", "Oferta pracy", "Inne" )
create_date = ""
author = ""
phone_number = ""
email = ""
price = 0
views = 0

def dopiszDaneDoPliku():

    linie = ['\n']
    global title, description, category, author, phone_number, email, price, views
    title = input("Wpisz tytul ogloszenia: ")
    linie.append(title)
    description = input("Wpisz opis ogloszenia: ")
    linie.append(description)
    category = input("Wpisz kategorie ogloszenia: ")
    linie.append(category)
    author = input("Wpisz autora ogloszenia: ")
    linie.append(author)
    phone_number = input("Wpisz numer telefonu autora ogloszenia: ")
    linie.append(phone_number)
    email = input("Wpisz email kontakowy autora ogloszenia: ")
    linie.append(email)
    price = input("Wpisz cene: ")
    linie.append(price)
    views = input("Wpisz liczbe wyswietlen ogloszenia: ")
    linie.append(str(views))

    with open('ogloszenie2.txt', 'a') as f:
            f.write('\n'.join(linie))

dopiszDaneDoPliku()