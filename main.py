import calculations as calc

command_dictionary = {
        'pinfo': 'New empty Capsules made of HPMC (Hydroxypropylmethylcellulose)',
        'pbuy': "CREATE NEW PRODUCT BUY TEXT",
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
        'wenexpirelul': "CREATE NEW EXPIRE TEXT",
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
    
def handle_input():
        try:
            behavior = command_dictionary[input()]
            print(behavior)
            extended_functionality(behavior)
        except:
            print("Im sorry, I didn't understand your input. Can you repeat, please?")
                
def extended_functionality(behavior):
    if behavior == 'pbuy':
        calc.order_product()
    elif behavior == 'wenexpirelul':
        calc.get_expiry_date()


if __name__ == '__main__':
    print_welcome()
    handle_input()

#while loop, bis dismiss command kommt
#text 4 github push
