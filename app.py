#functions of inventory-management-system





#function to put product
def put_product (name, quantity, price) :
    products[name] = { 
        'price': price ,
        'quantity': quantity 
    }
 
#a function for canceling a product from list
def cancel_product(name):
    if name in products:
        products.pop(name)
    else:
        print("Product not found.")

#a function for changing quantity of a product  
def update_quantity (pname,newquantity):
   products[pname]['quantity'] =  newquantity 


#function to see list of available operations

def list_options ():
 
  print( "this is list of options: ")
  
  print( "1.show products")
  
  print( "2. insert products")
  
  print( "3.updating a product's quantity ")
  
  print( "4.to search for a product") 
  
  print( "5.canceling products") 


#a fuction for looking for a product 
def search_prod ( sname): 
    if sname in products: 
        print (sname, " is in products' list ") 
    else:  
        print (sname, "isn't in product's list ") 


products = {  'laptop' :{ 'price': 10000, 'quantity': 400 },
              'iPod'   :{'price': 4400, 'quantity': 100},
              'iPad'   : { 'price': 4800, 'quantity': 500},
              'speaker': {'price': 1000, 'quantity': 87}, 
           } 


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
