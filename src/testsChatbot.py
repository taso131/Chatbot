import textprints as prints
import library as lib
import discountlogic as dc
import os

#Try to print an invoice
def test_print_invoice(firstName = "t1st", secondName = "t2st", testAmount = 3):
    customer_data = [firstName, secondName, testAmount]
    customer_data.append(dc.get_total_sum(customer_data))
    prints.print_invoice(customer_data)

    
#def write_order_into_database(firstName, lastName, amount_ordererd):
#    with open((os.path.join(os.path.join(os.environ['USERPROFILE']))) + "\\Desktop\\database.txt", "a") as f:
#        f.writelines(firstName + ";" + lastName + ";" + str(amount_ordererd) + "\n")
        
if __name__ == "__main__":
    lib.write_order_into_database(["first","one", 2, 33.3])
    test_print_invoice()
    
    
