import textprints as text
import asyncio
import time
import datetime
import os
import discountlogic


class BotLogic():

    def __init__(self) -> None:
        self.new_customer = True  # would come from a database
        self.steps_of_progress = {
            'pbuy': 0,
        }
        self.customer_data = []
        self.last_function = ''

    def extended_functionality(self, behavior):
        if behavior == 'pbuy':
            self.set_zero()
            self.last_function = behavior
            return self.ask_for_capsules()
        elif self.last_function == 'pbuy':
            return self.ask_for_information(behavior)
        elif behavior == 'wenexpirelul':
            return get_expiry_date()
        elif behavior == 'hlppls':
            return asyncio.run(try_to_reach_live_support())
        else:
            return "Im sorry, I didn't understand your input. Can you repeat, please?"

    def set_zero(self):
        for step in self.steps_of_progress:
            self.steps_of_progress[step] = 0
        self.customer_data = []


    def ask_for_information(self, params):
        answer = ''
        if self.steps_of_progress['pbuy'] == 1:
            answer = "What's your Firstname?"
        elif self.steps_of_progress['pbuy'] == 2:
            answer = "What's your Lastname?"
        elif self.steps_of_progress['pbuy'] == 3:
            self.customer_data.append(params)
            self.customer_data.append(
                float(int(self.get_total_sum()*100)/100))
            answer = text.print_invoice(self.customer_data)
            self.set_zero()
        self.customer_data.append(params)
        self.steps_of_progress["pbuy"] += 1
        return answer

    def ask_for_capsules(self):
        self.set_zero()
        self.steps_of_progress["pbuy"] += 1
        return """We are happy, to welcome you as a customer. Please, follow the next steps to create your invoice:<br>
                    How many units of Capsules do you want to buy? 1 Unit = 1.000 Capsules"""

################################### TASO



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
    #while not int, re-ask
    return [first_name, last_name, units_to_purchase]



def write_order_into_database(customer_data):
   
    with open((os.path.join(os.path.join(os.environ['USERPROFILE']))) + "\\Desktop\\database.txt", "a") as f:
        
        f.writelines(customer_data[0] + ";" 
                     + customer_data[1] + ";" 
                     + str(customer_data[2]) + ";"
                     + str(customer_data[3]) + "\n")