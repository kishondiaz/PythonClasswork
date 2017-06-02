
# MAIN FUNCTION
def main():
    
    bill = eval(input("Enter bill amount: "))
    percent= eval(input("Enter tip amount: "))
    tip = bill * percent
    total = tip + bill
    print("the tip is: ",tip)
    print("this is the total: ",total)

main()
