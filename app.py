
print( "Have a nice trial! welcome to this  inventory-management-system  ") 
print( "to show list-options enter y ") 
o = input() 
 

while o != 'y' or o != 'Y':
              print ("invalid! please if you want to exit enter e else enter y")
              o= input()
       
while o == 'y' or 'Y': 
       
     list_options()
     print ("enter 1,2,3,4,5 for your options  ")
     x = input()
    
   
     if x == '1': 
          for name, info in products.items():
              print(f"{name}: Price = {info['price']}, Quantity = {info['quantity']}")
    
       
    elif x == '2':
        put_product(sname, squantity, sprice) 
    

    elif x == '3':

        while k == '0':
               k == '1'
               print ("what product you want to update ? ") 
               s = input()
               if search_prod(s) == False:
                      print( "there's no", s, "in product's list shown")  
                      k == '0'
               
        print ("what is new quantity?") 
        new_quantity = int( input("new quantity: "))
        update_quantity(s, new_quantity)
    
    elif x == '4':
       
        print ("what is product's name you want to search for ?") 
        s = input ()
        if search_prod (s) : 
               print( s, "is in products' list") 
        else: 
               print( s, "isn't in products' list")
   
     elif x == '5': 
           while k == '0':
                  k == '1'
                  print ("what product you want to omit ? ") 
                  s = input()
                  if search_prod(s) == False:
                         print( "there's no", s, "in product's list shown")  
                         k == '0'
           cancel_product(s)
    
     print("enter y to continue else type n ") 
     o = tolower(input())
     if o == 'n': 
            print (" ----Exit!----")   
            break  
