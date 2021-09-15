import os

new_customer: bool  # would come from a database

def get_total_sum(customer_data) -> float:
    # the prices are for capsules with no filling and no aroma
    amount_to_buy = float(customer_data[2])
    if first_time_customer(customer_data):  # need to be added.
        print("worked")
    else:
        print("worked again, but denied")
       # if amount_to_buy < 3:
            # 10 euro discount / 1pcs. = 50% / 2pcs. = 25%
       #     return(amount_to_buy * 19.99-10)
      #  else:
     #       return(amount_to_buy * 15.99)  # 20% discount
    #else:
    #    if amount_to_buy < 3:
   #         return(amount_to_buy * 19.99)  # no discount
  #      else:
##            return(amount_to_buy * 17.99)  # 10% discount


def first_time_customer(customer_data) -> bool:
    first_name = customer_data[0]
    last_name = customer_data[1]
    
    file = open((os.path.join(os.path.join(os.environ['USERPROFILE']))) + "\\Desktop\\database.txt", "r")
    
    for line in file:
        if line.startswith(f"{first_name};{last_name}"):
            return False
    
    return True