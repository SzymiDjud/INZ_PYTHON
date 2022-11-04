from ad import Ad
class Ads(Ad):
    def __init__ (self):
        obiekt1= Ad("Testowy tytul", "Testowy opis", "Testowa kategoria",
        "Testowa data", "Testowy autor",999111222,"testowyemail@email.com",200,100)
        obiekt2=Ad("Drugi tytul", "Testowy opis", "Testowa kategoria",
        "Testowa data", "Testowy autor",999111222,"testowyemail@email.com",400,100)
        obiekt3=Ad("Trzeci tytul", "Testowy opis", "Testowa kategoria",
        "Testowa data", "Testowy autor",999111222,"testowyemail@email.com",600,100)
        self.ads = [obiekt1,obiekt2,obiekt3]

    def print(self):
        for obiekt in self.ads:
            obiekt.print()

