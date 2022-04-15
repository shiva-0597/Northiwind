from flask_sqlalchemy import SQLAlchemy

db=SQLAlchemy()

class OrderModel(db.Model):
    __tablename__ = 'orders'
    orderId = db.Column(db.String(30), primary_key=True)
    customerId = db.Column(db.String(5), nullable=False)
    employeeId = db.Column(db.Integer, nullable=False)
    orderDate = db.Column(db.DateTime, nullable=True)
    requiredDate = db.Column(db.DateTime, nullable=True)
    shippedDate = db.Column(db.DateTime, nullable=True)
    shipVia = db.Column(db.Integer, nullable=False)
    freight = db.Column(db.Float, nullable=False)
    shipName = db.Column(db.String(40), nullable=False)
    shipAddress = db.Column(db.String(60), nullable=False)
    shipCity = db.Column(db.String(15), nullable=False)
    shipRegion = db.Column(db.String(15), nullable=False)
    shipPostalCode = db.Column(db.String(10), nullable=False)
    shipCountry = db.Column(db.String(15), nullable=False)
    def __init__(self,orderId,customerId,employeeId,orderDate,requiredDate,shippedDate,shipVia,freight,shipName,shipAddress,shipCity,shipRegion,shipPostalCode,shipCountry):
        self.orderId=orderId
        self.customerId=customerId
        self.employeeId=employeeId
        self.orderDate=orderDate
        self.requiredDate=requiredDate
        self.shippedDate=shippedDate
        self.shipVia=shipVia
        self.freight=freight
        self.shipName=shipName
        self.shipAddress=shipAddress
        self.shipCity=shipCity
        self.shipRegion=shipRegion
        self.shipPostalCode=shipPostalCode
        self.shipCountry=shipCountry

    def output(self) -> dict:
        return {
            "orderId": self.orderId,
            "customerId": self.customerId,
            "employeeId": self.employeeId,
            "orderDate": self.orderDate,
            "requiredDate": self.requiredDate,
            "shippedDate": self.shippedDate,
            "shipVia": self.shipVia,
            "freight": self.freight,
            "shipName": self.shipName,
            "shipAddress": self.shipAddress,
            "shipCity": self.shipCity,
            "shipRegion": self.shipRegion,
            "shipPostalCode": self.shipPostalCode,
            "shipCountry": self.shipCountry
        }