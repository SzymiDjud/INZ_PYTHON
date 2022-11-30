title = ""
description = ""
category = ""
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

def wypiszDane():
   print(title)
   print(description)
   print(category)
   print(author)
   print(phone_number)
   print(email)
   print(price)
   print(views)

def znajdzFrazeWTekscie(tekst,fraza):
    wynik = tekst.find(fraza)

    print(wynik)

def manipulacjeLancuchami(tekst):
    print("Pierwsze 5 znakow zmiennej: " + tekst[:5])
    print("Znaki od 2 do 5 zmiennej: " + tekst[2:5])
    print("Znaki tekstu jako male litery: " + tekst.lower())
    print("Znaki tekstu jako WIELKIE litery: " + tekst.upper())
    print("Usuniecie bialych znakow z poczatku i konca tekstu: " + tekst.strip())
    print("Zamiana jednego znaku na wybrany inny: " + tekst.replace("a","b"))
    print("Polaczenie kilku metod: " + tekst.upper().replace("A","B").replace("B","CDE"))
    nowyTekst = " ".join(tekst.split())
    print("Usuniecie bialych znakow ze srodka lancucha: " + nowyTekst)

znajdzFrazeWTekscie("Testowa fraza", "fraza")
manipulacjeLancuchami(" Ananas ")
manipulacjeLancuchami(" Ananas  i  BAN               AN ")



