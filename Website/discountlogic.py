import os

product_cost: float = 19.99
product_cost_with_flavour = 23.99
tier1_promotion = 3
tier2_promotion = 10

# Decimal numbers are percentage numbers
promotions_dictionary = {
    'no_discount': 1,
    'first_order_50_off': 0.5,
    'first_order_rest_25_off': 0.75,
    'more_than_3': 0.9,
    'more_than_10': 0.8
}


def get_total_sum(customer_data) -> float:
    amount_to_buy = float(customer_data[0])

    if first_time_customer(customer_data):
        return calculations_for_new_customer(amount_to_buy)
    else:
        return calculations_for_normal_customers(amount_to_buy)


def calculations_for_normal_customers(amount_to_buy) -> float:
    if amount_to_buy < tier1_promotion:
        return (amount_to_buy * product_cost) * float(promotions_dictionary['no_discount'])

    elif amount_to_buy >= tier1_promotion and amount_to_buy <= tier2_promotion:
        return (amount_to_buy * product_cost) * float(promotions_dictionary['more_than_3'])

    else:
        return (amount_to_buy * product_cost) * float(promotions_dictionary['more_than_10'])


def calculations_for_new_customer(amount_to_buy) -> float:
    if amount_to_buy < 2:
        return product_cost * float(promotions_dictionary['first_order_50_off'])

    else:
        first_one_50_off = product_cost * \
            float(promotions_dictionary['first_order_50_off'])
        not_qualified_amount = amount_to_buy - 1
        left_ones_25_off = (not_qualified_amount * product_cost) * \
            float(promotions_dictionary['first_order_rest_25_off'])

        return first_one_50_off + left_ones_25_off


def first_time_customer(customer_data) -> bool:
    first_name = customer_data[1]
    last_name = customer_data[2]

    file = open((os.path.join(os.path.join(
        os.environ['USERPROFILE']))) + "\\Desktop\\database.txt", "r")

    for line in file:
        if line.startswith(f"{first_name};{last_name}"):
            return False

    return True
