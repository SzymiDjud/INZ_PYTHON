class Ad:

    def __init__(self,title,description,category,create_date,author,phone_number,email,price,views):
        self.title = title
        self.description = description
        self.category = category
        self.create_date = create_date
        self.author = author
        self.phone_number = phone_number
        self.email = email
        self.price = price
        self.views = views

    def print(self):
        print(self.title, self.description, self.category, self.create_date, self.author,self.phone_number,self.email,self.price,self.views)