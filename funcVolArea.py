##name:Kishon Diaz
##program name: funcVolArea.py



import math
message = "{0:0>2}"

def area(radius):
    while True:
        rad = input("Enter a number to get the Area of a sphere: ")
        if rad == "":
            return 0
        rad = int(rad)
        if rad < 1:
            print("Number must be higher then 0")
            break
        else:
            sArea = round(4*math.pi*rad**2,2)
            print(message.format(sArea))
            break
def volume(radius):
    while True:
        rad = input("Enter a number to get the Volume of a sphere: ")
        if rad == "":
            return 0
        rad = int(rad)    
        if rad < 1:
            print("Number must be higher then 0 ")
            break
        else:
            sVolume = round(4/3*math.pi*rad**3, 2)
            print(message.format(sVolume))
            break
def operation():
    choice = input("Press A for Area and V for Volume of a sphere Else Enter to quit: ")
    if choice == "a" or choice == "A":
        choice ="1"
    elif choice == "v" or choice == "V":
        choice ="2"
    elif choice =="":
        print("You have Exited the program")
        return 0
    
    return int(choice)
        
def main():
    while True:
        try:
            radius = operation()

            if radius == 1:
                area(radius)
            elif radius == 2:
                volume(radius)
            elif radius == 0:
                return 0
        except ValueError:
            print("you entered in a wrong input! ")
    


if __name__ == "__main__":
    main()
