#functions of inventory-management-system





#function to put product
def put_product () :
        print("what is product's name?") 
        name = input( 'name: ')
        
        print ("what is product's quantity?")
        quantity = int(input ( 'quantity: '))
        
        print( "what is product's price? ") 
        price = float(input ('price: '))
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


products = {  'laptop' :{ 'price': 10000    , 'quantity': 400 },
              'iPod'   :{ 'price': 4400     , 'quantity': 100 },
              'iPad'   :{ 'price': 4800     , 'quantity': 500 },
              'speaker':{ 'price': 1000     , 'quantity': 87  }, 
           } 

