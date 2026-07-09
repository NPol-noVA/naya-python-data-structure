#functions of inventory-management-system





#function to put product
def put_product (name, quantity, price) :
    products[name] = { 
        'price': price ,
        'quantity': quantity 
    }
 
#a function for canceling a product from list
def cancel_product ( name): 
    products.pop('name')

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
