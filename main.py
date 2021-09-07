from datetime import date

string = ""
new_customer = False #Need to be replaced with a call from a database
# Press Umschalt+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_welcome():
    # Use a breakpoint in the code line below to debug your script.
    print("Hello dear Customer. Welcome to our \"live\" Support.")  # Press Strg+F8 to toggle the breakpoint.
    print("""How may I help you today?\n
    Type in one of the following for easy and quick support:\n
    pinfo = Get Product information.\n
    pbuy = Buy the Product. You'll be asked after sending for the amount.\n
    hlppls = Talk to my supervisor.\n
    extendedhlppls = Get more help commands""") 
    
#rabatt system
def print_invoice(capsule_units_to_purchase):
    print("|-------------------------------------------|")
    print(f"| --- {get_total_sum(capsule_units_to_purchase)} € ---|")
    print("|-------------------------------------------|")

def get_total_sum(capsule_units):
    # the prices are for capsules with no filling and no aroma    
    if new_customer: # need to be added.
        if capsule_units < 3:
            return(capsule_units*19.99-10) # 10 euro discount / 1pcs. = 50% / 2pcs. = 25%
        else:
            return(capsule_units*15.99) # 20% discount
    else:
        if capsule_units < 3:
            return(capsule_units*19.99) # no discount
        else:
            return(capsule_units*17.99) # 10% discount                                          

def handle_input():
    command = input()
    if command == "pinfo":
        print("New empty Capsules made of HPMC (Hydroxypropylmethylcellulose)")
    if command == 'pbuy':
            print("How many units of Capsules do you want to buy? 1 Unit = 1.000 Capsules")
            capsule_units_to_purchase = input()
            print_invoice(capsule_units_to_purchase)
            
    elif command == 'hlppls':
            print("ww1")
    elif command == 'extendedhlppls':
            print("""
            icantwait = Wanna know when your Package might arrive?\n
            idontwantitanymore = Unhappy with our Service? :( Just tell us! We'll find a solution\n
            wenexpirelul = Best before date. You'll be asked for the month you'll want to order\n
            canipaywithbitcoins = What payment methods do we accept? Also want to know weather we accept installment plans?\n
            isyourstuffevengood = Worrying that those capsules are out of bad quality? Or not as described? Just see one of our reviews\n
            howdoiusethisshhh = Need explanation on how to improve your usage with our HPMC-Capsules? Say no more!\n
            """)
    elif command == 'icantwait':
            print("The moment you order, you'll get it by 2-4 Days in Europe. 7-10 Days in America and 10-14 Days worldwide")
    elif command == 'idontwantitanymore':
            print(
                "You may return your purchase for no reason in 14 days and you can apply for a return within 90 days "
                "if there is a reason")
    elif command == 'wenexpirelul':
            print(get_expiry_date())
    elif command == 'canipaywithbitcoins':
            print("You can pay with BTC, ETH, ADA, ONE and RBC")
    elif command == 'isyourstuffevengood':
            print("Still not 100% if it fits for you? Look at the dozens of reviews we already have gotten since launch")
    elif command == 'howdoiusethisshhh':
            print("For detailed instructions you can watch our video on youtube.com")

        #best before date = 1 year from date given the person wants to order

def get_expiry_date() -> date:
    expiry_date = date.today()
    expiry_date.year = date.year + 1

    return expiry_date



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_welcome()
    handle_input()

#while loop, bis dismiss command kommt
#text 4 github push

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
