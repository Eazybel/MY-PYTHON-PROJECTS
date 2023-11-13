menu={
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}



man=[]
while True:
     try:               
            val=input("item: ")   
            val=val.title()
            if val in menu:
              man.append(menu.get(val))
            elif val not in menu:
                print(f"error: {val}")
                break
     except KeyboardInterrupt:
             tan=sum(man)
             print(f"\nTotal: ${tan:.2f}")
             

                
            


        
