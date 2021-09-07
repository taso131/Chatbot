import product
from struct import Struct

command_dictionary = {
        'pinfo': 'New empty Capsules made of HPMC (Hydroxypropylmethylcellulose)',
        'pbuy': product.get_product_pricing(),
        'hlppls': 'ww1',
        'extendedhlppls': """
            icantwait = Wanna know when your Package might arrive?\n
            idontwantitanymore = Unhappy with our Service? :( Just tell us! We'll find a solution\n
            wenexpirelul = Best before date. You'll be asked for the month you'll want to order\n
            canipaywithbitcoins = What payment methods do we accept? Also want to know weather we accept installment plans?\n
            isyourstuffevengood = Worrying that those capsules are out of bad quality? Or not as described? Just see one of our reviews\n
            howdoiusethisshhh = Need explanation on how to improve your usage with our HPMC-Capsules? Say no more!\n """,
        'icantwait': 'The moment you order, you\'ll get it by 2-4 Days in Europe. 7-10 Days in America and 10-14 Days worldwide',
        'idontwantitanymore': 'You may return your purchase for no reason in 14 days and you can apply for a return within 90 days if there is reason',
        'wenexpirelul': product.get_expiry_date(),
        'canipaywithbitcoins': 'You can pay with BTC, ETH, ADA, ONE and RBC',
        'isyourstuffevengood': 'Still not 100% if it fits for you? Look at the dozens of reviews we already have gotten since launch',
        'howdoiusethisshhh': 'For detailed instructions you can watch our video on youtube.com',
        'nothxbye' : 'kthxbye'
        }

def print_welcome():
    print("Hello dear Customer. Welcome to our \"live\" Support.")
    print("""How may I help you today?\n
    Type in one of the following for easy and quick support:\n
    pinfo = Get Product information.\n
    pbuy = Buy the Product. You'll be asked after sending for the amount.\n
    hlppls = Talk to my supervisor.\n
    extendedhlppls = Get more help commands""") 
    

def print_order_instructions() -> list[str]:
    print("How many units of Capsules do you want to buy? 1 Unit = 1.000 Capsules")
    units_to_purchase = input()
    print("What's your Firstname?")
    first_name = input()
    print("What's your Lastname?")
    last_name = input()
    return [units_to_purchase, first_name, last_name]

#rabatt system
def print_invoice(customer_data):
    print( "|--------------------------------------------------------------------------|")
    print(f"|-------------- Dear {customer_data[1], customer_data[2]} ---------------- |")
    print(f"| --- We are happy for your purchase of {customer_data[0]} * 1000 Caps --- |")
    print(f"| ---------------------- {product.get_total_sum(customer_data[0])} € --------------------- |")
    print( "|--------------------------------------------------------------------------|")