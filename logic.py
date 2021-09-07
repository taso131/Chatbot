
import dialogs


def handle_input():
        quitprogram = False
        try:
                print(dialogs.command_dictionary[input()])    
        except:
                print("Im sorry, I didn't understand your input. Can you repeat, please?")

if __name__ == '__main__':
    dialogs.print_welcome()
    handle_input()

#while loop, bis dismiss command kommt
#text 4 github push
