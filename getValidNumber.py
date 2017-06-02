# Validate Input
# Require user to input a numerc value >= 1

def getX():
    prompt = "Enter a value for X, or press ENTER to quit: "
    errorMessage = "\nInvalid value (Must enter a number >= 1 or press ENTER)\n"
    
    while True:
        choice = input(prompt)
        if choice == "":
            return 0
        try:
            n = int(choice)
            if n < 1:
                print(errorMessage)
            else:
                break
        except ValueError:
            print(errorMessage)
    return n

def main():
    while True:
        x = getX()
        if x == 0:
            print("Exit.")
            break
        print("The number you entered is: ", x)

if __name__ == "__main__":
    main()
