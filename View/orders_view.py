from Models.orders import OrderModel,db
from flask import request
from flask_restful import Resource

class OrdersViews(Resource):
    def get(self):
        orders =OrderModel.query.all()
        return {"orders":[x.output() for x in orders]} 

class OrderViews(Resource):

    def get(self,OrderID) -> dict:
        order=OrderModel.query.filter_by(OrderID=OrderID).first()
        if order:
            return order.output()
        return {"Output_message":"Customer not found"},404

    def put(self,OrderID:int) -> dict:
        req=request.get_json()
        order=OrderModel.query.filter_by(OrderID=OrderID).first()
        if order:
            OrderModel.EmployeeID=req["EmployeeID"]
            OrderModel.CustomerID=req["CustomerID"]
            OrderModel.freight=req["Freight"]
            OrderModel.OrderDate=req["OrderDate"]
            OrderModel.RequiredDate=req["RequiredDate"]
            OrderModel.ShipAddress=req["ShipAddress"]
            OrderModel.ShipCity=req["ShipCity"]
            OrderModel.ShipCountry=req["ShipCountry"]
            OrderModel.ShipName=req["ShipName"]
            OrderModel.ShippedDate=req["ShippedDate"]
            OrderModel.ShipRegion=req["ShipRegion"]
            OrderModel.ShipPostalCode=req["ShipPostalCode"]
            OrderModel.ShipVia=req["ShipVia"]  
        else:
            order=OrderModel(OrderID=OrderID, customerId=req["CustomerID"], freight=req["Freight"],
                    shipAddress=req["ShipAddress"],
                    employeeId=req["EmployeeID"],orderDate=req["OrderDate"], shipCity=req["ShipCity"],
                    shipCountry=req["ShipCountry"], shipName=req["ShipName"],shippedDate=req["ShippedDate"],
                    shipRegion=req["ShipRegion"],shipPostalCode=req["ShipPostalCode"],shipVia=req["ShipVia"],RequiredDate=req["RequiredDate"])
        
        db.session.add(order)
        db.session.commit()
        return {"Output_message":"Input Inserted"}

    def delete(self,OrderID:int):
        order=OrderModel.query.filter_by(OrderID=OrderID).first()
        if order:
            db.session.delete(order)
            db.session.commit()
            return {"output_message":"deleted"}
        return {"Output_message":"order not found"},404

class OrderHistoryView(Resource):
    def get(self,customerId:str):
        orderhistory=OrderModel.query.filterby(customerId=customerId).first()
        if orderhistory:
            return{
                "customerId":customerId,
                "orders":list(x.output() for x in orderhistory)
            }
        return{
            "output_message":"Customer is not found"
        }


