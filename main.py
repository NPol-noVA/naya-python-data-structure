from functions import (
    put_product,
    cancel_product,
    list_options,
    search_prod, update_quantity,)

products = {  'laptop' :{ 'price': 10000, 'quantity': 400 },
              'iPod'   :{'price': 4400, 'quantity': 100},
              'iPad'   : { 'price': 4800, 'quantity': 500},
              'screen' : {'price': 1000, 'quantity': 87}, 
           } 

products = {  'laptop' :{ 'price': 10000, 'quantity': 400 },
              'iPod'   :{'price': 4400, 'quantity': 100},
              'iPad'   : { 'price': 4800, 'quantity': 500},
              'screen' : {'price': 1000, 'quantity': 87}, 
           } 
print( "Have a nice trial! welcome to this  inventory-management-system  ") 
print( "to show list-options enter y ") 
o = input() 


while o == 'y': 
    if o == 'y':
        list_options()
    print ("enter 1,2,3,4,5 for your options  ")
    x=input()
 
    if x == '1': 
        print (products)
    
    elif x == '2':
        print("what is product's name?") 
        sname = input( 'name: ')
        print ("what is product's quantity?")
        squantity = input ( 'quantity: ') 
        print( "what is product's price? ") 
        sprice = input ('price: ') 

        put_product(sname, sprice, squantity) 
    
    elif x == '3':
        print ("what product you want to update ? ") 
        s = input()
        print ("what is new quantity?") 
        new_quantity = input("new quantity: ") 
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
    s = input()
    if o == 'n': 
      print (" ----Exit!----")   
      break  
