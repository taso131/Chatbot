from datetime import date

def get_expiry_date() -> str:
    expiry_date = date.today()
#    expiry_date.year = date.year + 1
    #best before date = 1 year from date given the person wants to order
    return expiry_date
    

def get_total_sum(amount_to_buy) -> int:
    return amount_to_buy
    #discount

#customer_data = List[units_to_purchase, first_name, last_name]
def order_product():
    customer_data = print_order_instructions()
    customer_data.append(get_total_sum(1)) #rabatt system
    print_invoice(customer_data)
    
def print_order_instructions() -> list[str]:
    print("How many units of Capsules do you want to buy? 1 Unit = 1.000 Capsules")
    units_to_purchase = input()
    print("What's your Firstname?")
    first_name = input()
    print("What's your Lastname?")
    last_name = input()
    return [units_to_purchase, first_name, last_name]

def print_invoice(customer_data):
    print( "|--------------------------------------------------------------------------|")
    print(f"|-------------- Dear {customer_data[1], customer_data[2]} ---------------- |")
    print(f"| --- We are happy for your purchase of {customer_data[0]} * 1000 Caps --- |")
    print(f"| ---------------------- {customer_data[4]} € --------------------- |")
    print( "|--------------------------------------------------------------------------|")







    
