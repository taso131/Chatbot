import textprints as prints
import functions as funcs
import os

#Try to print an invoice
def test_print_invoice(firstName = "t1st", secondName = "t2st", testAmount = 3):
    customer_data = [firstName, secondName, testAmount, funcs.get_total_sum(2)]
    prints.print_invoice(customer_data)
    write_order_into_database(customer_data)

    
def write_order_into_database(firstName, lastName, amount_ordererd):
    with open((os.path.join(os.path.join(os.environ['USERPROFILE']))) + "\\Desktop\\database.txt", "w") as f:
        f.writelines(firstName + ";" + lastName + ";" + str(amount_ordererd) + "\n")
        
if __name__ == "__main__":
    write_order_into_database("a","a",2)
    
    
