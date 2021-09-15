import library as lib

command_dictionary = {
    'pinfo': 'We offer empty Capsules made of HPMC (Hydroxypropylmethylcellulose), but also prefilled ones with a variety of aromas, too!',
    'hlppls': 'Hold on for a minute, we\'ll try to connect you to the next supervisor we can reach',
    'extendedhlppls': """
            icantwait = Want to know when your Package might arrive?\n
            idontwantitanymore = Unhappy with our Service? :( Just tell us! We'll find a solution\n
            wenexpirelul = Best before date. You'll be asked for the month you'll want to order\n
            canipaywithbitcoins = What payment methods do we accept? Also want to know wether you can pay in rates?\n
            isyourstuffevengood = Worrying that those capsules are made with bad quality? Or not as described? Just take a look at one of our reviews\n
            howdoiusethisshhh = Need explanation on how to improve your usage with our HPMC-Capsules? Say no more!\n """,
        'icantwait': 'The moment your order comes into our system, you\'ll usually get it by 2-4 Days in Europe. 7-10 Days in America and 10-14 Days worldwide',
        'idontwantitanymore': 'You may return your purchase for no reason in 14 days and you can apply for a return within 90 days if there is reason',
        'wenexpirelul': "Our capsules are guaranteed to at least have a best before date two years in the future, the moment you order",# Hier muss ein Datetime geprinted werden, was currenttime + (year+1) ist
        'canipaywithbitcoins': 'You can pay with BTC, ETH, ADA, ONE and RBC. But we also accept PayPal, Visa, Mastercard and EU-SEPA direct debit, including wire transfer',
        'isyourstuffevengood': 'Still not 100% if it fits for you? Look at the dozens of reviews we already have gotten since launch',
        'howdoiusethisshhh': 'For detailed instructions you can watch our video on https://www.youtube.com/watch?v=dQw4w9WgXcQ',
        #'nothxbye' : 'I hope that my responses where useful for you. Thank your for contacting our support. Have a nice day!' #Muss gleichzeitig eine extended functionality sein und die while schleife beenden
        }

def print_welcome():
    return """Hello dear Customer. Welcome to our \"live\" Support.
    How may I help you today?\n
    Type in one of the following for easy and quick support:\n
    pinfo = Get Product information.\n
    pbuy = Buy the Product. You'll be asked after sending for the amount.\n
    hlppls = Talk to my supervisor.\n
    extendedhlppls = Get more help commands"""
    # print("Hello dear Customer. Welcome to our \"live\" Support.")
    # print("""How may I help you today?\n
    # Type in one of the following for easy and quick support:\n
    # pinfo = Get Product information.\n
    # pbuy = Buy the Product. You'll be asked after sending for the amount.\n
    # hlppls = Talk to my supervisor.\n
    # extendedhlppls = Get more help commands""")


def print_invoice(customer_data):
    print( "|-------------------------------------------------------------|")
    print(f"|------------------- Dear {customer_data[0], customer_data[1]} -------------------- |")
    print(f"| ----- We are happy for your purchase of {customer_data[2]} * 1000 Caps ----- |")
    print(f"| -------------------- {customer_data[3]} € ----------------------- |")
    print( "|--------------------------------------------------------------|")
    lib.write_order_into_database(customer_data)
    


def print_rating():
    print("""
░░░░░░░░░▄░░░░░░░░░░░░░░▄░░░░
░░░░░░░░▌▒█░░░░░░░░░░░▄▀▒▌░░░   Very guud
░░░░░░░░▌▒▒█░░░░░░░░▄▀▒▒▒▐░░░
░░░░░░░▐▄▀▒▒▀▀▀▀▄▄▄▀▒▒▒▒▒▐░░░
░░░░░▄▄▀▒░▒▒▒▒▒▒▒▒▒█▒▒▄█▒▐░░░
░░░▄▀▒▒▒░░░▒▒▒░░░▒▒▒▀██▀▒▌░░░       Much wow 5/5
░░▐▒▒▒▄▄▒▒▒▒░░░▒▒▒▒▒▒▒▀▄▒▒▌░░
░░▌░░▌█▀▒▒▒▒▒▄▀█▄▒▒▒▒▒▒▒█▒▐░░
░▐░░░▒▒▒▒▒▒▒▒▌██▀▒▒░░░▒▒▒▀▄▌░
░▌░▒▄██▄▒▒▒▒▒▒▒▒▒░░░░░░▒▒▒▒▌░
▀▒▀▐▄█▄█▌▄░▀▒▒░░░░░░░░░░▒▒▒▐░       15/10 dogs are good boys after those caps
▐▒▒▐▀▐▀▒░▄▄▒▄▒▒▒▒▒▒░▒░▒░▒▒▒▒▌
▐▒▒▒▀▀▄▄▒▒▒▄▒▒▒▒▒▒▒▒░▒░▒░▒▒▐░
░▌▒▒▒▒▒▒▀▀▀▒▒▒▒▒▒░▒░▒░▒░▒▒▒▌░           11/10
░▐▒▒▒▒▒▒▒▒▒▒▒▒▒▒░▒░▒░▒▒▄▒▒▐░░
░░▀▄▒▒▒▒▒▒▒▒▒▒▒░▒░▒░▒▄▒▒▒▒▌░░           Such wow
░░░░▀▄▒▒▒▒▒▒▒▒▒▒▄▄▄▀▒▒▒▒▄▀░░░
░░░░░░▀▄▄▄▄▄▄▀▀▀▒▒▒▒▒▄▄▀░░░░░
░░░░░░░░░▒▒▒▒▒▒▒▒▒▒▀▀░░░░░░░░
          
          
          ░░░░░░░░░░▄▄█▀▀▄░░░░
░░░░░░░░▄█████▄▄█▄░░░░
░░░░░▄▄▄▀██████▄▄██░░░░
░░▄██░░█░█▀░░▄▄▀█░█░░░▄▄▄▄              \"Thanks to those new caps, I can finally clear the levels without falling even once off the map\"
▄█████░░██░░░▀▀░▀░█▀▀██▀▀▀█▀▄                   - Mega Man
█████░█░░▀█░▀▀▀▀▄▀░░░███████▀
░▀▀█▄░██▄▄░▀▀▀▀█▀▀▀▀▀░▀▀▀▀
░▄████████▀▀▀▄▀░░░░
██████░▀▀█▄░░░█▄░░░░
░▀▀▀▀█▄▄▀░██████▄░░░░
░░░░░░░░░█████████░░░░
""")