
print( "Have a nice trial! welcome to this  inventory-management-system  ") 
print( "to show list-options enter y ") 
o = input() 


while o == 'y': 
       
     list_options()
     print ("enter 1,2,3,4,5 for your options  ")
     x = input()
    
    if x == '1': 
        for name, info in products.items():
            print(f"{name}: Price = {info['price']}, Quantity = {info['quantity']}")
    
    elif x == '2':
        print("what is product's name?") 
        sname = input( 'name: ')
        print ("what is product's quantity?")
        squantity = int(input ( 'quantity: '))
        print( "what is product's price? ") 
        sprice = float(input ('price: '))
        put_product(sname, squantity, sprice) 
    
    elif x == '3':
        print ("what product you want to update ? ") 
        s = input()
        print ("what is new quantity?") 
        new_quantity = int( input("new quantity: "))
        update_quantity(s, new_quantity)
    
    elif x == '4':
        print ("what is product's name you want to search for ?") 
        s = input ()
        search_prod (s)
    
    elif x == '5': 
        print ( "what product you want to omit? ") 
        s=input () 
        cancel_product(s) 
        
    print("enter y to continue else type n ") 
    o = input()
    if o == 'n': 
      print (" ----Exit!----")   
      break  
