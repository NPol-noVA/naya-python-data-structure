# naya-python-data-structures


## Intro
This project is an **Inventory Management System** written in Python. It allows users to manage a collection of products by performing common inventory operations such as adding, removing, updating, searching, and displaying products.

The project is organized into two files:
* **app.py** – runs the program and handles user interaction.
* **data.py** – stores the inventory and contains all functions that manage the data.
---

## Python Data Structures
Python provides four main built-in data structures:

### 1. List
* Ordered
* Changeable (mutable)
* Allows duplicate values

A list is useful when the order of items matters and duplicate items are allowed.


### 2. Tuple

* Ordered
* Unchangeable (immutable)
* Allows duplicate values

A tuple is useful for storing data that should not change after it is created.

### 3. Dictionary

* Stores data as **key–value pairs**
* Changeable (mutable)
* Keys must be unique

A dictionary is the best choice when data needs to be accessed quickly using a unique key.


### 4. Set

* Unordered
* Changeable (mutable)
* Does not allow duplicate elements

A set is useful when only unique values are needed.

---

## Why a Dictionary Was Chosen

The inventory is stored as a **dictionary of dictionaries**.

Each product has a unique name, making the product name an excellent dictionary key. This allows products to be searched, updated, or removed quickly without checking every product one by one.

A list of dictionaries could also store the products, but searching for a product would require iterating through the entire list until the correct product is found. Using a dictionary provides faster and simpler access by product name.

---

## Dictionary Structure

Each product is represented by its own dictionary containing its quantity and price.

Example:

```python
products = {
    "Laptop": {
        "quantity": 400,
        "price": 10000
    },
    "iPad": {
        "quantity": 500,
        "price": 4800
    }
}
```

In this structure:

* The **product name** is the dictionary key.
* The **value** is another dictionary containing the product's quantity and price.

---

## Features

The Inventory Management System provides the following operations:

* Add a new product
* Remove an existing product
* Update a product's quantity
* Search for a product by name
* Display all products
* Continue performing multiple operations without restarting the program

---

## How to Run

Run the application using:

```bash
python app.py
```

---

## error handelding and debugging: 
I have put everything with error handeling in my first assignment so it was not required big changes
I only : 
change  

    while o != 'y' or o != 'Y': 
        o= input ()
    while o == 'y' or o == 'Y': 
        /block
change: 
s= input to s= tolower(input()) 
because there's case sensetivity 

that is all because i have previousely avoid error from users and searched for each input before making operations
inputs were also accurate: int , float, were assigned to their variable to avoid problems
