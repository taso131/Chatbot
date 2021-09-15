import textprints as prints
import library as lib
import random
import os

#Try to print an invoice
def test_print_invoice(testAmount = 0, firstName = "t1st", secondName = "t2st"):
    customer_data = [testAmount, firstName, secondName, lib.get_total_sum(2)]
    prints.print_invoice(customer_data)#lib.get_total_sum(random.randint(0, 100))

    
def write_order_into_database(firstName, lastName, amount_ordererd):
    with open((os.path.join(os.path.join(os.environ['USERPROFILE']))) + "\\Desktop\\database.txt", "w") as f:
        f.writelines(firstName + ";" + lastName + ";" + str(amount_ordererd) + "\n")
        
if __name__ == "__main__":
    write_order_into_database("a","a",2)
    
    
