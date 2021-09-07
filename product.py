from datetime import date
import dialogs

def get_expiry_date() -> str:
    expiry_date = date.today()
#    expiry_date.year = date.year + 1
    #best before date = 1 year from date given the person wants to order
    return expiry_date
    
#customer_data = List[units_to_purchase, first_name, last_name]
def get_product_pricing():
    customer_data: dialogs.print_order_instructions()
    dialogs.print_invoice(customer_data)
        
def get_total_sum(amount_to_buy):
    return
    #discount