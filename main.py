import library as lib
import textprints as text
import asyncio 
import time
    
def handle_input():
    while True:
        try:
            input_dictionary_key = input()
            dictionary_result = text.command_dictionary[input_dictionary_key]
            print(dictionary_result)
            
            if input_dictionary_key == 'nothxbye':
                break
            
            extended_functionality(input_dictionary_key)
            time.sleep(2)
            print("Is there anything else I can help you with? If not, just type in 'kthxbye'")
            
        except KeyError: 
            print("Im sorry, I didn't understand your input. Can you repeat, please?")
                
def extended_functionality(behavior):
    if behavior == 'pbuy':
        customer_data = lib.order_product()
        text.print_invoice(customer_data)
        
    elif behavior == 'wenexpirelul':
        lib.get_expiry_date()
        
    elif behavior == 'hlppls':
        asyncio.run(lib.try_to_reach_live_support()) #hier printed er nur ein mal den text, async noch nicht korrekt


if __name__ == '__main__':
    text.print_welcome()
    handle_input()
    print("I'm glad we could help. Enjoy your day! :)")
