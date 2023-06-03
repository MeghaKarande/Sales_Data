

from flask import Flask, jsonify, render_template, request

from project_app.utils import SalesData

# Creating instance here
app = Flask(__name__)


@app.route("/") 
def hello_flask():
    print("Welcome to Sales Price Prediction System")   
    return render_template("index.html")


@app.route("/predict_charges", methods = ["POST", "GET"])
def get_sales_price():
    if request.method == "GET":
        print("We are in a GET Method")


        Item_Weight = int(request.args.get("Item_Weight"))
        Item_Fat_Content = request.args.get("Item_Fat_Content")
        Item_Visibility = float(request.args.get("Item_Visibility"))
        Item_MRP = float(request.args.get("Item_MRP"))
        Outlet_Establishment_Year = int(request.args.get("Outlet_Establishment_Year"))
        Outlet_Size = request.args.get("Outlet_Size")
        Outlet_Location_Type = request.args.get("Outlet_Location_Type")
        Item_Type = request.args.get("Item_Type")
        Outlet_Identifier = request.args.get("Outlet_Identifier")
        Outlet_Type = request.args.get("Outlet_Type")


        print("-------------------- Item_Weight, Item_Fat_Content, Item_Visibility, Item_MRP, Outlet_Establishment_Year, Outlet_Size, Outlet_Location_Type, Item_Type, Outlet_Identifier, Outlet_Type -----------------")

        sales = SalesData(Item_Weight, Item_Fat_Content, Item_Visibility, Item_MRP, Outlet_Establishment_Year, Outlet_Size, Outlet_Location_Type, Item_Type, Outlet_Identifier, Outlet_Type)
        charges = sales.get_predicted_charges()
        
        return render_template("index.html", prediction = charges)
    # return jsonify({"Result": f"Predicted Charges is {charges} /- Rs."})

print("__name__ -->", __name__)

if __name__ == "__main__":
    app.run(host= "0.0.0.0", port= 5005, debug = False)  