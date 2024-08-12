#function
def clear_screen():
    print("\033[H\033[J", end="")

def sum_numbers(first_number, second_number):
    clear_screen()
    result = first_number + second_number
    print(first_number, "+", second_number, "=", result)

def sub_numbers(first_number, second_number):
    clear_screen()
    result = first_number - second_number
    print(first_number, "-", second_number, "=", result)

def multp_numbers(first_number, second_number):
    clear_screen()
    result = first_number * second_number
    print(first_number, "*", second_number, "=", result)

def divd_numbers(first_number, second_number):
    clear_screen()
    result = first_number / second_number
    print(first_number, "/", second_number, "=", result)


#main
while(True):
    
    print("Choose an operation")
    choice = int(input("1 - add\n2 - multiply\n3 - subtract\n4 - divide\n5 - exit\n"))
    clear_screen()

    if choice < 1 or choice > 5:
        clear_screen()
        print("opcao invalida")
        continue
    
    elif choice == 5:
        clear_screen()
        print("exiting the program...") 
        break

    first_number = float(input("Enter the first number: "))
    second_number = float(input("Enter the second number: "))

    swt_choice = {
        1 : sum_numbers,
        2 : multp_numbers,
        3 : sub_numbers,
        4 : divd_numbers
    }

    if choice in swt_choice:
        clear_screen()
        swt_choice[choice](first_number, second_number)
        