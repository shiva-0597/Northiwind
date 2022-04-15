# from Models.product import Product,db
from Models.customer import CustomerModel,db
# from Models.orders import orderModel,db
from flask import request
from flask_restful import Resource
class CustomersViews(Resource):
    def get(self):
        customers=CustomerModel.query.all()
        return {"customers":[x.output() for x in customers]}

class CustomerViews(Resource):
    def get(self, CustomerID:str) -> dict:
        customer=CustomerModel.query.filter_by( CustomerID=CustomerID).first()
        if customer:
            return customer.output()
        return {"Output_message":"Customer not found"},404

    def put(self,CustomerID:str):
        req=request.get_json()
        customer=CustomerModel.query.filter_by(CustomerID=CustomerID).first()
        if customer:
            CustomerModel.CompanyName=req["CompanyName"]
            CustomerModel.Address=req["Address"]
            CustomerModel.City=req["City"]
            CustomerModel.ContactName=req["ContactName"]
            CustomerModel.ContactTitle=req["ContactTitle"]
            CustomerModel.Country=req["Country"]
            CustomerModel.Fax=req["Fax"]
            CustomerModel.Phone=req["Phone"]
            CustomerModel.Region=req["Region"]
            CustomerModel.PostalCode=req["PostalCode"]
        else:
            customer=CustomerModel(CustomerID=CustomerID,CompanyName=req["CompanyName"],
                                ContactName=req["ContactName"],Phone=req["Phone"],
                                City=req["City"],Region=req["Region"],PostalCode=req["PostalCode"],
                                Fax=req["Fax"],Country=req["Country"],ContactTitle=req["ContactTitle"],Address=req["Address"])
        
        db.session.add(customer)
        db.session.commit()
        return {"Output_message":"Input Inserted"}

    def delete(self,CustomerID:str):
        customer=CustomerModel.query.filter_by(CustomerID=CustomerID).first()
        if customer:
            db.session.delete(customer)
            db.session.commit()
            return {"output_message":"deleted"}
        return {"Output_message":"Customer not found"},404

