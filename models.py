from main import db

class Tourist(db.Model):
    __tablename__='toursits'
    id=db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String)
    username=db.Column(db.String)
    password=db.Column(db.String)
    
    def __init__(self,name,username,password) :
        self.name=name
        self.username=username
        self.password=password


class Site(db.Model):
    __tablename__='sites'
    id=db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String)
    location=db.Column(db.String)
    description=db.Column(db.String)
    price=db.Column(db.Float)

    def __init__(self,name,location,description,price):
        self.name=name
        self.location=location
        self.description=description
        self.price=price


class Hotel(db.Model):
    __tablename__='hotels'
    id=db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String)
    site=db.Column(db.String)
    location=db.Column(db.String)
    description=db.Column(db.String)
    price=db.Column(db.Float)


    def __init__(self,name,location,site,description,price):
        self.name=name
        self.location=location
        self.site=site
        self.description=description
        self.price=price


class Travel(db.Model):
    __tablename__='travels'
    id=db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String)
    site=db.Column(db.String)
    location=db.Column(db.String)
    description=db.Column(db.String)
    price=db.Column(db.Float)


    def __init__(self,name,location,site,description,price):
        self.name=name
        self.location=location
        self.site=site
        self.description=description
        self.price=price