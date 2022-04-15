from flask_sqlalchemy import SQLAlchemy

db=SQLAlchemy()
class CustomerModel(db.Model):
    __tablename__="customers"
    CustomerID = db.Column(db.String(5), primary_key=True)
    CompanyName = db.Column(db.String(40), nullable=False)
    contactName = db.Column(db.String(30), nullable=False)
    contactTitle = db.Column(db.String(30), nullable=False)
    address = db.Column(db.String(60), nullable=False)
    city = db.Column(db.String(15), nullable=False)
    region = db.Column(db.String(15), nullable=False)
    PostalCode= db.Column(db.String(30), nullable=False)
    country = db.Column(db.String(15), nullable=False)
    phone = db.Column(db.String(24), nullable=False)
    fax = db.Column(db.String(24), nullable=False)
    def __init__(self, CustomerID,CompanyName,ContactName,ContactTitle,Address,City,Region,Country,Phone,Fax,PostalCode):
        self.CustomerID = CustomerID
        self.CompanyName=CompanyName
        self.ContactName=ContactName
        self.ContactTitle=ContactTitle
        self.Address=Address
        self.City=City
        self.Region=Region
        self.Country=Country
        self.Phone=Phone
        self.Fax=Fax
        self.PostalCode=PostalCode
    def output(self):
        return {
            "customerId": self.CustomerID,
            "companyName": self.CompanyName,
            "contactName": self.contactName,
            "contactTitle": self.contactTitle,
            "address": self.address,
            "city": self.city,
            "region": self.region,
            "country": self.country,
            "phone": self.phone,
            "fax": self.fax,
            "PostalCode": self.PostalCode,
        }
