from src.fish import Fish

def main():
    fih = Fish()
    swim = True

    while swim == True:
        print_menu()
        swim = user_input(fih)

def print_divider():
    print("--------------------------------------------------")

def print_menu():
    print_divider()
    print('''What do you want to do?\n
0. Blub blub.
1. Get the flag :00000 (yasss!!!)
2. idk
3. fih
4. quit''')

def user_input(fih: Fish) -> bool:
    selection = input("\nInput (please input the appropriate number): ")
    print_divider()
    print("")

    try:
        selection = int(selection)
    except ValueError:
        print("Fih no understand; why thou try to confu fih? :(")
    else:
        match selection:
            case 0:
                print(fih.blub())
            case 1:
                print(fih.get_flag())
            case 2:
                print("I don't know either.")
            case 3:
                fih.fih().show()
            case 4:
                print("See ya!")

                return False
            case _:
                print("Sorry?")
    finally:
        print("")

    return True

if __name__ == "__main__":
    main()
