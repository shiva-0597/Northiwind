from Models.orders import OrderModel,db
from flask import request
from flask_restful import Resource

class OrdersViews(Resource):
    def get_all_orders(self):
        orders =OrderModel.query.all()
        print(orders)
        return {"orders":[x.output() for x in orders]} 

class OrderViews(Resource):

    def get_orders(self,orderId:str) -> dict:
        order=OrderModel.query.filter(orderId=orderId).first()
        if order:
            return OrderModel.output()
        return {"Output_message":"Customer not found"},404

    def put_orders(self,orderId:str) -> dict:
        req=request.get_json()
        order=OrderModel.query.filterby(orderId=orderId).first()
        if order:
            OrderModel.employeeId=req["employeeId"]
            OrderModel.customerId=req["customerId"]
            OrderModel.freight=req["freight"]
            OrderModel.amount=req["amount"]
            OrderModel.orderDate=req["orderDate"]
            OrderModel.requiredDate=req["requiredDate"]
            OrderModel.shipAddress=req["shipAddress"]
            OrderModel.shipCity=req["shipCity"]
            OrderModel.shipCountry=req["shipCountry"]
            OrderModel.shipName=req["shipName"]
            OrderModel.shippedDate=req["shippedDate"]
            OrderModel.shipRegion=req["shipRegion"]
            OrderModel.shipPostalCode=req["shipPostalCode"]
            OrderModel.shipVia=req["shipVia"]  
        else:
            order=OrderModel(orderId=orderId, customerId=req["customerId"], freight=req["freight"],
                    amount=req["amount"], shipAddress=req["shipAddress"],
                    employeeId=req["employeeId"],orderDate=req["orderDate"], shipCity=req["shipCity"],
                    shipCountry=req["shipCountry"], shipName=req["shipName"],shippedDate=req["shippedDate"],
                    shipRegion=req["shipRegion"],shipPostalCode=req["shipPostalCode"],shipVia=req["shipVia"])
        
        db.session.add(order)
        db.session.commit()
        return {"Output_message":"Input Inserted"}

    def delete_orders(self,orderId:str):
        order=OrderModel.query.filterby(orderId=orderId).first()
        if order:
            db.session.delete(order)
            db.commit()
            return {"output_message":"deleted"}
        return {"Output_message":"order not found"},404

    def order_history(self,customerId:str):
        order=OrderModel.query.filterby(customerId=customerId).first()
        if order:
            return{
                "customerId":customerId,
                "orders":list(x.output() for x in order)
            }
        return{
            "output_message":"Customer is not found"
        }


