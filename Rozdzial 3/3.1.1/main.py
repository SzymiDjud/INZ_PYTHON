title = ""
description = ""
category = ""
create_date = ""
author = ""
phone_number = ""
email = ""
price = 0
views = 0

title = input("Wpisz tytul ogloszenia: ")
description = input("Wpisz opis ogloszenia: ")
category = input("Wpisz kategorie ogloszenia: ")
author = input("Wpisz autora ogloszenia: ")
phone_number = input("Wpisz numer telefonu autora ogloszenia: ")
email = input("Wpisz email kontakowy autora ogloszenia: ")

price = int((input("Wpisz cene: ")))
views = int((input("Wpisz liczbe wyswietlen ogloszenia: ")))

print(price + views)
print(int(phone_number) + float(price))

