from app import app, db
import unittest
import json
from Models.orders import OrderModel
from Models.product import ProductModel
from Models.customer import CustomerModel


class Testing(unittest.TestCase):
    def test_orders(self):
        test = app.test_client(self)
        response = test.get('/orders')
        status_code = response.status_code
        self.assertEqual(status_code, 200)

    def test_customers(self):
        tester = app.test_client(self)
        response = tester.get('/customers')
        status_code = response.status_code
        self.assertEqual(status_code, 200)

    def test_products(self):
        tester = app.test_client(self)
        response = tester.get('/product')
        status_code = response.status_code
        self.assertEqual(status_code, 200)

    def test_order_content(self):
        tester = app.test_client(self)
        response = tester.get('/order/10248')
        print(response)
        status_code = response.status_code
        self.assertEqual(status_code, 200)

    def test_product_content(self):
        tester = app.test_client(self)
        response = tester.get('/products/1')
        status_code = response.status_code
        self.assertEqual(status_code, 200)

    def test_customer_content(self):
        tester = app.test_client(self)
        response = tester.get('/customer/VINET')
        status_code = response.status_code
        self.assertEqual(status_code, 200)

    def test_order_insert(self):
        tester = app.test_client(self)
        order_id = 11077
        data = {
            "CustomerID": 11077,
            "EmployeeID": 4,
            "OrderDate": None,
            "RequiredDate": None,
            "ShippedDate": None,
            "ShipVia": 2,
            "Freight": 38.28,
            "ShipName": "Bon app'",
            "ShipAddress": "12 rue des Bouchers",
            "ShipCity": "Marseille",
            "ShipRegion": "NULL",
            "ShipPostalCode": "13008",
            "ShipCountry": "France"
        }
        response = tester.put(
            '/order/11077', data=json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content_type, 'application/json')
        self.assertEqual(response.get_json(), {"Output_message":"Input Inserted"})
        
        data["EmployeeID"] = 3
        response = tester.put(
            '/order/11077', data=json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content_type, 'application/json')
        self.assertEqual(response.get_json(), {"Output_message":"Input Inserted"})

    def test_order_delete(self):
        tester = app.test_client(self)
        order_id = 11077
        data = {
            "OrderID": 11077,
            "CustomerID": 11077,
            "EmployeeID": 4,
            "OrderDate": None,
            "RequiredDate": None,
            "ShippedDate": None,
            "ShipVia": 2,
            "Freight": 38.28,
            "ShipName": "Bon app'",
            "ShipAddress": "12 rue des Bouchers",
            "ShipCity": "Marseille",
            "ShipRegion": "NULL",
            "ShipPostalCode": "13008",
            "ShipCountry": "France"
        }
        order = OrderModel(order_id, data["CustomerID"], data["EmployeeID"], data["OrderDate"],
                           data["RequiredDate"], data["ShippedDate"], data["ShipVia"], data["Freight"],
                           data["ShipName"], data["ShipAddress"], data["ShipCity"], data["ShipRegion"],
                           data["ShipPostalCode"], data["ShipCountry"])


        response = tester.delete('/order/11077')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content_type, 'application/json')
        self.assertEqual({"output_message":"deleted"}, response.get_json())

        response = tester.delete('/order/11090')
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.content_type, 'application/json')
        self.assertEqual(response.get_json(), {"Output_message":"order not found"})

    def test_customer_insert(self):
        tester = app.test_client(self)
        data = {
            "CompanyName": "Vins et alcools Chevalier",
            "ContactName": "Paul Henriot",
            "ContactTitle": "Accounting Manager",
            "Address": "59 rue de l'Abbaye",
            "City": "Reims",
            "Region": "NULL",
            "PostalCode": "51100",
            "Country": "France",
            "Phone": "26.47.15.10",
            "Fax": "26.47.15.11"
        }
        response = tester.put(
            '/customer/VARNI', data=json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content_type, 'application/json')
        self.assertEqual(response.get_json(), {"Output_message":"Input Inserted"})
        # Testing update
        data["City"] = "Chandigarh"
        response = tester.put(
            '/customer/VARNI', data=json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content_type, 'application/json')
        self.assertEqual(response.get_json(), {"Output_message":"Input Inserted"})

    def test_customer_delete(self):
        tester = app.test_client(self)
        CustomerID = 'VARNI'
        data = {
            "CompanyName": "Vins et alcools Chevalier",
            "ContactName": "Paul Henriot",
            "ContactTitle": "Accounting Manager",
            "Address": "59 rue de l'Abbaye",
            "City": "Reims",
            "Region": "NULL",
            "PostalCode": "51100",
            "Country": "France",
            "Phone": "26.47.15.10",
            "Fax": "26.47.15.11"
        }
        customer = CustomerModel(CustomerID=CustomerID, CompanyName=data["CompanyName"], ContactName=data["ContactName"], ContactTitle=data["ContactTitle"],
                                 Address=data["Address"], City=data["City"], Region=data["Region"], PostalCode=data["PostalCode"],
                                 Country=data["Country"], Phone=data["Phone"], Fax=data["Fax"])

        with app.app_context():
            db.session.add(customer)
            db.session.commit()

        response = tester.delete('/customer/VARNI')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content_type, 'application/json')
        self.assertEqual({"output_message":"deleted"}, response.get_json())

        # Checking for non-existing record
        response = tester.delete('/customer/KAUKA')
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.content_type, 'application/json')
        self.assertEqual(response.get_json(), {"Output_message":"Customer not found"})

    def test_product_insert(self):
        tester = app.test_client(self)
        ProductID = 78
        data = {
            "ProductName": "Original Frankfurter",
            "SupplierID": 12,
            "CategoryID": 2,
            "QuantityPerUnit": "12 boxes",
            "UnitPrice": 13.0,
            "UnitsInStock": 32,
            "UnitsOnOrder": 0,
            "ReorderLevel": 15,
            "Discontinued": False

        }
        response = tester.put(
            '/product/78', data=json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, 404)
        data["SupplierID"] = 11
        response = tester.put(
            '/product/78', data=json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, 404)
        
        with app.app_context():
            product = ProductModel.query.filter_by(
                ProductID=ProductID).first()
        if product:
            with app.app_context():
                db.session.delete(product)
                db.session.commit()

    def test_product_delete(self):
        tester = app.test_client(self)
        ProductID = 20
        data = {
            "ProductName": "Original Frankfurter",
            "SupplierID": 12,
            "CategoryID": 2,
            "QuantityPerUnit": "12 boxes",
            "UnitPrice": 13.0,
            "UnitsInStock": 32,
            "UnitsOnOrder": 0,
            "ReorderLevel": 15,
            "Discontinued": False
        }
        product = ProductModel(ProductID=ProductID,SupplierID=data["SupplierID"],CategoryID=data["CategoryID"],
                        QuantityPerUnit=data["QuantityPerUnit"],UnitsInStock=data["UnitsInStock"],
                        ReorderLevel=data["ReorderLevel"],UnitPrice=data["UnitPrice"],Discontinued=data["Discontinued"],
                        ProductName=data["ProductName"],UnitsOnOrder=data["UnitsOnOrder"])
        

        with app.app_context():
            db.session.add(product)
            db.session.commit()

        response = tester.delete('/product/20')
        self.assertEqual(response.status_code, 404)

        response = tester.delete('/product/79')
        self.assertEqual(response.status_code, 404)


if __name__ == '__main__':
    unittest.main()
   