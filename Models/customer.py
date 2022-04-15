from flask_sqlalchemy import SQLAlchemy

db=SQLAlchemy()
class CustomerModel(db.Model):
    __tablename__="customers"
    customerId = db.Column(db.String(5), primary_key=True)
    companyName = db.Column(db.String(40), nullable=False)
    contactName = db.Column(db.String(30), nullable=False)
    contactTitle = db.Column(db.String(30), nullable=False)
    address = db.Column(db.String(60), nullable=False)
    city = db.Column(db.String(15), nullable=False)
    region = db.Column(db.String(15), nullable=False)
    postalCode = db.Column(db.String(10), nullable=False)
    country = db.Column(db.String(15), nullable=False)
    phone = db.Column(db.String(24), nullable=False)
    fax = db.Column(db.String(24), nullable=False)
    def __init__(self,customerId,companyName,contactName,contactTitle,address,city,region,postalCode,country,phone,fax):
        self.customerId = customerId
        self.companyName=companyName
        self.contactName=contactName
        self.contactTitle=contactTitle
        self.address=address
        self.city=city
        self.region=region
        self.postalCode=postalCode
        self.country=country
        self.phone=phone
        self.fax=fax
    def output(self):
        return {
            "customerId": self.customerId,
            "companyName": self.companyName,
            "contactName": self.contactName,
            "contactTitle": self.contactTitle,
            "address": self.address,
            "city": self.city,
            "region": self.region,
            "postalcode": self.postalcode,
            "country": self.country,
            "phone": self.phone,
            "fax": self.fax
        }
