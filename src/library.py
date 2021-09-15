from datetime import datetime
import time
import os
import discountlogic

def get_expiry_date():
    current_date = datetime.now()
    expiry_date_year = int(current_date.strftime('%Y')) + 2
    expiry_date_month = current_date.strftime('%m')
    print(f"If you order this month, your product will have a best before date of {expiry_date_month} / {expiry_date_year}")

async def try_to_reach_live_support():
    for i in range(0, 10):
        print("Hold on for a minute, we will try to connect you. Estimated time: 1 Min.")
        time.sleep(3)
        
    print("Connection timed out. Seems like there is no one left. Or maybe no one cares... Bad luck, my friend")

#customer_data = List[first_name, last_name, units_to_purchase, total amount]
def order_product() -> list[str]:
    customer_data = print_order_instructions()
    customer_data.append(discountlogic.get_total_sum(customer_data))  # rabatt system
    return customer_data

def print_order_instructions() -> list[str]:
    print("What's your Firstname?")
    first_name = input()
    print("What's your Lastname?")
    last_name = input()
    print("How many units of Capsules do you want to buy? 1 Unit = 1.000 Capsules")
    units_to_purchase = str(input())
    return [first_name, last_name, units_to_purchase]



def write_order_into_database(customer_data):
   
    with open((os.path.join(os.path.join(os.environ['USERPROFILE']))) + "\\Desktop\\database.txt", "a") as f:
        
        f.writelines(customer_data[0] + ";" 
                     + customer_data[1] + ";" 
                     + str(customer_data[2]) + ";"
                     + str(customer_data[3]) + "\n")