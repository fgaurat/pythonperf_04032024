from CustomerDAO import CustomerDAO

def main():
    dao = CustomerDAO('tp08\customer_db.db')
    customers = dao.findAll()

    for customer in customers:
        print(customer)

if __name__=='__main__':
    main()
