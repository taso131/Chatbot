from datetime import date
import time


def get_expiry_date() -> str:
    expiry_date = date.today()
#    expiry_date.year = date.year + 1
    #best before date = 1 year from date given the person wants to order
    return expiry_date
    

def get_total_sum(amount_to_buy) -> int:
    return amount_to_buy
    #discount

#customer_data = List[units_to_purchase, first_name, last_name]
def order_product() -> list[str]:
    customer_data = print_order_instructions()
    customer_data.append(get_total_sum(1)) #rabatt system
    return customer_data
    
async def try_to_reach_live_support():
    for i in range(0,10):
        print("Hold on for a minute, we will try to connect you. Estimated time: 1 Min.")
        await time.sleep(3)
    print("Connection timed out. Seems like there is no one left. Or maybe no one cares... Bad luck, my friend")
    
def print_order_instructions() -> list[str]:
    print("How many units of Capsules do you want to buy? 1 Unit = 1.000 Capsules")
    units_to_purchase = input()
    print("What's your Firstname?")
    first_name = input()
    print("What's your Lastname?")
    last_name = input()
    return [units_to_purchase, first_name, last_name]








    
