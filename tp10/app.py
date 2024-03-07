from flask import Flask,render_template
from CustomerDAO import CustomerDAO

app = Flask(__name__)

@app.route("/hello")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/moche")
def moche():
    dao = CustomerDAO('customer_db.db')
    customers = dao.findAll()
    html = ""
    
    for customer in customers:
        html +=f"<li>{customer.first_name} {customer.last_name}</li>"

    return f"<ul>{html}</ul>"


@app.route("/")
def index():
    dao = CustomerDAO('customer_db.db')
    customers = dao.findAll()

    return render_template('customers.html',customers=customers )
   