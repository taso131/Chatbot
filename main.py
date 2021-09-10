import library as lib
import textprints as text
    
def handle_input():
        try:
            input_dictionary_key = input()
            dictionary_result = text.command_dictionary[input_dictionary_key]
            print(dictionary_result)
            extended_functionality(input_dictionary_key)
        except:
            print("Im sorry, I didn't understand your input. Can you repeat, please?")
                
def extended_functionality(behavior):
    if behavior == 'pbuy':
        customer_data = lib.order_product()
        text.print_invoice(customer_data)
    elif behavior == 'wenexpirelul':
        lib.get_expiry_date()


if __name__ == '__main__':
    text.print_welcome()
    handle_input()

#while loop, bis dismiss command kommt
#text 4 github push
