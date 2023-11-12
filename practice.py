def num():
    number=put()
    if number > 0:
        print("its' negative")
    elif number < 0:
        print("its' posetive")


def put():
    while True:
        try:
            n=int(input("enter your number: "))
            return n
        except ValueError:
            print("it's not a number")
    
    
    
        
        
num()
        
    
    
