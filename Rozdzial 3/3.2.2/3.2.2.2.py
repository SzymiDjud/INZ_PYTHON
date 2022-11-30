from ad import Ad
class specialAd(Ad):
    def __init__ (self,title,description,
                  category,create_date,author,phone_number,email,price,views,special):
        super().__init__(title,description,category,create_date,author,phone_number,email,price,views)
        self.special = special


