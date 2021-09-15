import textprints as text
import asyncio
import time
import datetime


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

    def get_total_sum(self) -> float:
        # the prices are for capsules with no filling and no aroma
        amount = int(self.customer_data[0])
        if self.new_customer:  # need to be added.
            if amount < 3:
                # 10 euro discount / 1pcs. = 50% / 2pcs. = 25%
                return(amount*19.99-10)
            else:
                return(amount*15.99)  # 20% discount
        else:
            if amount < 3:
                return(amount*19.99)  # no discount
            else:
                return(amount*17.99)  # 10% discount

# customer_data = List[units_to_purchase, first_name, last_name]

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


def get_expiry_date():
    current_date = datetime.datetime.now()
    # addiere 1 jahr auf current date
    # date(current_date.year + 2, current_date.month, current_date.day)
    best_before_date = current_date + datetime.timedelta(years=1)
    # date(startDate.year + 1, startDate.month
    return f"""Our capsules are guaranteed to at least have a best before date two years in the future, the moment you order
            If you order this month, your product will have a best before date of {best_before_date}"""


async def try_to_reach_live_support():
    for i in range(0, 2):
        time.sleep(3)
    return "Connection timed out. Seems like there is no one left. Or maybe no one cares... Bad luck, my friend"
