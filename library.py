import datetime


def get_expiry_date():
    current_date = datetime.date()
    #addiere 1 jahr auf current date
    datetime.replace(year=self.year,
    current_date = datetime.replace(year=self.year +1)
    #date(startDate.year + 1, startDate.month
    print(f"If you order this month, your product will have a best before date of {best_before_date}")
    
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
        time.sleep(3)
    print("Connection timed out. Seems like there is no one left. Or maybe no one cares... Bad luck, my friend")
    
def print_order_instructions() -> list[str]:
    print("How many units of Capsules do you want to buy? 1 Unit = 1.000 Capsules")
    units_to_purchase = input()
    print("What's your Firstname?")
    first_name = input()
    print("What's your Lastname?")
    last_name = input()
    return [units_to_purchase, first_name, last_name]








    
