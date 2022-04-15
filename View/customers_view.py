from Models.product import ProductModel,db
from Models.customer import CustomerModel,db
from Models.orders import OrderModel,db
from flask import request
from flask_restful import Resource
class CustomersViews(Resource):
    def get_all_customers(self):
        customers=CustomerModel.query.all()
        print(customers)
        return {"customers":[x.output() for x in customers]}

class CustomerViews(Resource):
    def get_customers(self,customerId:str) -> dict:
        customer=CustomerModel.query.filter(customerId=customerId).first()
        if customer:
            return CustomerModel.output()
        return {"Output_message":"Customer not found"},404

    def put_customers(self,customerId:str):
        req=request.get_json()
        customer=CustomerModel.query.filterby(customerId=customerId).first()
        if customer:
            CustomerModel.companyName=req["companyName"]
            CustomerModel.address=req["address"]
            CustomerModel.city=req["city"]
            CustomerModel.contactName=req["contactName"]
            CustomerModel.contactTitle=req["contactTitle"]
            CustomerModel.country=req["country"]
            CustomerModel.fax=req["fax"]
            CustomerModel.phone=req["phone"]
            CustomerModel.region=req["region"]
            CustomerModel.postalCode=req["postalCode"]
        else:
            customer=CustomerModel(customerId=customerId,companyName=req["companyName"],
                                contactName=req["contactName"],phone=req["phone"],
                                city=req["city"],region=req["region"],postalCode=req["postalCode"],
                                fax=req["fax"],country=req["country"],contactTitle=req["contactTitle"],address=req["address"])
        
        db.session.add(customer)
        db.session.commit()
        return {"Output_message":"Input Inserted"}

    def delete_customers(self,customerId:str):
        customer=CustomerModel.query.filterby(customerId=customerId).first()
        if customer:
            db.session.delete(customer)
            db.commit()
            return {"output_message":"deleted"}
        return {"Output_message":"Customer not found"},404

