import datetime
import time

new_customer = True  # would come from a database


def get_expiry_date():
    current_date = datetime.datetime.now()
    # addiere 1 jahr auf current date
    # date(current_date.year + 2, current_date.month, current_date.day)
    best_before_date = current_date + datetime.timedelta(years=1)
    # date(startDate.year + 1, startDate.month
    print(
        f"If you order this month, your product will have a best before date of {best_before_date}")


def get_total_sum(amount_to_buy) -> float:
    # the prices are for capsules with no filling and no aroma
    if new_customer:  # need to be added.
        if amount_to_buy < 3:
            # 10 euro discount / 1pcs. = 50% / 2pcs. = 25%
            return(amount_to_buy*19.99-10)
        else:
            return(amount_to_buy*15.99)  # 20% discount
    else:
        if amount_to_buy < 3:
            return(amount_to_buy*19.99)  # no discount
        else:
            return(amount_to_buy*17.99)  # 10% discount

# customer_data = List[units_to_purchase, first_name, last_name] <- Diese kommentare sollten nicht im Code sein.
# Wenn du so einen Kommentar verwenden willst, dann in der Methode und """ am Anfang und Ende


def order_product() -> list[str]:
    """return List[units_to_purchase, first_name, last_name, amount_to_buy]"""
    # Ich glaube hier ist es besser ein tuple zurückzugeben, anstatt einer Liste
    customer_data = print_order_instructions()
    customer_data.append(get_total_sum(customer_data[0]))  # rabatt system
    return customer_data


async def try_to_reach_live_support():
    for i in range(0, 10):
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
