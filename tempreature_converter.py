import os
while True:
    print("\t\t Enter your choice\n1.C to F\n2.F to C\n3.C to K\n4.K to C\n5.F to K\n6.K to F")
    choice=int(input("...| "))
    if (choice < 0 or choice > 6):
        os.system('cls')
        print("please enter the number correctly")
    else:
        temp = int(input("enter the temperature: "))
        os.system('cls')
        if choice == 1:
            print(f"the value is: {temp*1.8+32}")
        elif choice == 2:
            print(f"the value is: {(temp-32)*0.5555555555555556}")
        elif choice == 3:
            print(f"the value is: {temp+273.15}")
        elif choice == 4:
            print(f"the value is: {temp - 273.15}")
        elif choice == 5:
            print(f"the value is: {(temp-32)*(0.5555556) + 273.15}")
        elif choice == 6:
            print(f"the value is: {(temp-273.15)*(9/5) + 32}")
       
    
    
    
    
    