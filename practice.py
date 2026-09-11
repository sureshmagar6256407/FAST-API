# from fastapi import FastAPI   
# app  = FastAPI()

# @app.get("/students") 
# def get_customer ()  : 
#     return { 
#         "students":["Ram","Sita","Hari"]
#     }


# from fastapi import FastAPI  
# app = FastAPI()

# @app.get("/students/{student_id}")
# def get_studentInfo  (student_id:int) : 
#     if student_id == 5 : 
#         return { 
#             "student_id" : student_id , 
#             "message" : "student found"
#         }
#     else  : 
#         return { 
#             "message" : "no student here"
#         }


# from fastapi import FastAPI 
# app = FastAPI()

# @app.get("/students")
# def response (city : str) : 
#     return { 
#         "city" : city , 
#         "message":f"student from {city}"
#     }



# from fastapi import FastAPI 
# app = FastAPI()

# @app.get("/students/{student_id}")
# def response ( student_id:int,details : bool) : 
#     return { 
#         "Student_id": student_id , 
#         "details" : details
#     }


# from fastapi  import FastAPI  
# from pydantic import BaseModel  

# app = FastAPI()

# class Students(BaseModel) : 
#     name : str  
#     age : int  
#     city : str

# @app.post("/students")
# def showInfo (student:Students) : 
#     return { 
#         "name":student.name , 
#         "age" :student.age , 
#         "city" :student.city 
#     }


# from fastapi import FastAPI  
# from pydantic import BaseModel
# app  = FastAPI   ()

# class Student ( BaseModel) : 
#     name : str  
#     math : int
#     science:int
#     english : int  


# @app.post ("/students")
# def show_students  (student:Student) : 
#     Total = student.math + student.english + student.science 
#     return { 
#         "name" : student.name , 
#         "total": Total,
#         "average" :  Total/3
#     }


# from fastapi import FastAPI  
# app  = FastAPI()

# @app.get("/products")
# def mobile_details (category:str, min_price:int): 
#     return { 
#         "category" : category   , 
#         "min_price" : min_price
#     }




# from fastapi import FastAPI  
# app = FastAPI()

# @app.get("/employees/{employee_id}")
# def show_employee(employee_id:int,department : str) : 
#     return { 
#         "employee_id" : employee_id , 
#         "department":department
#     }



# from fastapi import FastAPI 
# from pydantic import BaseModel
# from typing import Optional
# app  =FastAPI()

# class StudentMangement(BaseModel) : 
#     name :str  
#     age : int 
#     marks  :int  
#     city:str  

# students_obj = [
#     {"student_id":1,"name":"ram","age":20,"city":"kathmandu","marks":75} ,
#     {"student_id":2,"name":"sita","age":21,"city":"butwal","marks":85} ,
    

# ]


# @app.get("/students")  
# def show_student (city:Optional[str] =None) : 
#     if city : 
#         filtered_students = [s for s in students_obj if s["city"].lower()==city.lower()]
#         return filtered_students
#     return students_obj

# @app.get("/students/{student_id}")
# def get_student_by_id (student_id:int): 
#     for student in students_obj : 
#         if student["student_id"] ==student_id : 
#             return student

#     raise ValueError("student not found")


# @app.post("/students")
# def create_student(student:StudentMangement) : 
#     new_id = len(students_obj) +1   

#     student_data = student.model_dump()
#     student_data["student_id"] = new_id  

#     students_obj.append(student_data)
#     return {"message" : "student added succesfully ","data":student_data}





# from typing import Optional
# from fastapi import FastAPI  
# from pydantic import BaseModel
# app = FastAPI()

# class Product_details(BaseModel) : 
#     name :str  
#     category:str  
#     price:float  
#     stock :int
#     id:int

# available_product =  [ 
#     {"id":1, "name":"Samsung Mobile" , "category":"Mobile", "price":55550 , "stock":10} , 
#     {"id":2, "name":"Charger" , "category":"Electronic", "price":1000, "stock":50}, 
#     {"id":3, "name":"Fan" , "category":"Electronic", "price":10000 , "stock":33}

# ]


# @app.get("/products")
# def get_products(category:Optional[str] =None) : 
#     if category : 
#             filtered_product  = [i  for i in available_product   if i["category"].lower() == category.lower()]
#             return filtered_product   
#     return  { 
#         "details" :available_product
#     }
    

# @app.get("/products/{product_id}")
# def path_para (product_id :int) : 
#     for pro in available_product : 
#         if pro["id"] == product_id : 
#             return pro  
        
#     raise ValueError ("student not found ")


    


# @app.post("/products")
# def add_products(product: Product_details):
#     new_id = len(available_product) + 1
#     product_data = product.model_dump()
#     product_data["id"] = new_id
#     available_product.append(product_data)
#     return {
#         "message": "product added successfully",
#         "data": product_data,
#     }


# from fastapi import FastAPI    
# from typing import Optional

# app  = FastAPI()


# students = [
#     {"id": 1, "name": "Ram", "city": "Kathmandu"},
#     {"id": 2, "name": "Sita", "city": "Butwal"},
#     {"id": 3, "name": "Hari", "city": "Kathmandu"}
# ]
# @app.get("/students") 
# def get_city_by  (city:Optional[str] |None =None):    
#     if city : 
#         filtered_city  = [c for c in students if c["city"].lower() == city.lower()]
#         return filtered_city  
#     return students



# from fastapi import FastAPI  
# app =FastAPI()

# students = [
#     {"id": 1, "name": "Ram", "city": "Kathmandu"},
#     {"id": 2, "name": "Sita", "city": "Butwal"},
#     {"id": 3, "name": "Hari", "city": "Kathmandu"}
# ]

# @app.get("/students/{student_id}")
# def get_byId  (student_id:int) : 
#     for id in students : 
#         if id["id"] == student_id  : 
#             return id  
#     return {"message":"student not found"}


# from fastapi import FastAPI 
# from pydantic import BaseModel
# app  = FastAPI ()

# class StudentDetails(BaseModel) : 
#     name:str
#     age:int  
#     city:str  

# students = []

# @app.post("/students")  
# def create_student  (student:StudentDetails) : 
#     new_student = student.model_dump()   
#     students.append(new_student)   
#     return { 
#         "message":"student added successfully" , 
#         "data" : new_student
#     }


# from fastapi import FastAPI  
# from typing import Optional
# app  = FastAPI()

# products = [
#     {"id": 1, "name": "Laptop", "category": "Electronic", "price": 80000},
#     {"id": 2, "name": "Samsung", "category": "Mobile", "price": 50000},
#     {"id": 3, "name": "iPhone", "category": "Mobile", "price": 120000}
# ]

# @app.get("/products")
# def get_byCat (category:Optional[str] | None = None) : 
#     if category : 
#         filtered_cate  = [c for c in products if c["category"].lower() == category.lower()]
#         return filtered_cate  
#     return products



# from fastapi import FastAPI  
# from typing import Optional
# app  = FastAPI()

# products = [
#     {"id": 1, "name": "Laptop", "category": "Electronic", "price": 80000},
#     {"id": 2, "name": "Samsung", "category": "Mobile", "price": 50000},
#     {"id": 3, "name": "iPhone", "category": "Mobile", "price": 120000}
# ]

# @app.get("/products/{product_id}")
# def get_product(product_id:int ) : 
#     for jin  in products : 
#         if jin["id"] == product_id : 
#             return jin   
#     return {"error" : "Product not found"}


# @app.get("/products")
# def get_queerry (category:Optional[str] |None =None): 
#     if category : 
#         filtered_category  = [c for c in products if c["category"].lower() == category.lower()]
#         return filtered_category
#     return products



# from fastapi import FastAPI 
# from pydantic import BaseModel  
# from typing import Optional 

# app  = FastAPI()

# class CreateEmployees(BaseModel):     
#     name:str  
#     department:str 
#     salary:float

# employees = [
#     {"id": 1, "name": "Ram", "department": "IT", "salary": 50000},
#     {"id": 2, "name": "Sita", "department": "HR", "salary": 45000},
#     {"id": 3, "name": "Hari", "department": "IT", "salary": 60000}
# ]

# @app.get("/employees")
# def get_byQu   (department:Optional[str] |None =None) : 
#     if not department : 
#         return employees 

#     filtered_dep  = [de for de in employees if department.lower() == de["department"].lower()]
#     return filtered_dep

# @app.get("/employees/{employee_id}")
# def get_bypath   (employee_id :int) : 
#     for i  in employees : 
#         if i["id"]  == employee_id : 
#             return i 
#     return {"message" : "no employee id has in"}

# @app.post("/employees")
# def create_employee(employee:CreateEmployees) : 
#     new_id  = len(employees) + 1  
#     new_emplyee = employee.model_dump ()
#     new_emplyee["id"]  = new_id  
#     employees.append(new_emplyee)
#     return { 
#         "status" : "the student added"  ,
#         "data" : new_emplyee
#     }




'''
from fastapi import FastAPI  
from typing import Optional
from pydantic import BaseModel
app  = FastAPI ( )

class  AddFood(BaseModel) : 
    name : str  
    category:str  
    price: int  
    available :bool  

foods = [
    {
        "id": 1,
        "name": "Chicken Momo",
        "category": "Momo",
        "price": 180,
        "available": True
    },
    {
        "id": 2,
        "name": "Veg Chowmein",
        "category": "Chowmein",
        "price": 150,
        "available": True
    },
    {
        "id": 3,
        "name": "Pizza",
        "category": "Pizza",
        "price": 450,
        "available": False
    },
    {
        "id": 4,
        "name": "Buff Momo",
        "category": "Momo",
        "price": 200,
        "available": True
    }
]


@app.get("/foods")
def get_food(category :Optional[str] = None ,available:Optional[bool] = None) : 
    filtered_foods  = foods  
    if category : 
        filtered_foods = [ 
            f for f in filtered_foods  
            if f["category"].lower() ==category.lower()
        ]
    if  available is not None  :  
        filtered_foods   = [ 
            f for f in filtered_foods  
            if f.get("available") == available
        ]
    return filtered_foods

@app.get("/foods/available")
def get_available () : 
    return [food for food in foods if food.get("available")]

@app.get("/foods/{food_id}")
def get_foodBy_id (food_id:int) : 
    for i in foods : 
        if i["id"] == food_id : 
            return i
    return {"message":"Food not found"}


@app.post("/foods")
def add_new_food(food:AddFood) : 
    food_id = len(foods)+1   
    new_food   = food.model_dump()
    new_food["id"] = food_id  
    foods.append (new_food)
    return new_food
'''





'''
from fastapi  import FastAPI  
from typing import Optional    
from pydantic import BaseModel


app  = FastAPI ()

class Patient(BaseModel) : 
    name : str 
    age : int 
    department : str  
    admitted: bool 

patients = [
    {
        "id": 1,
        "name": "Ram",
        "age": 25,
        "department": "Cardiology",
        "admitted": True
    },
    {
        "id": 2,
        "name": "Sita",
        "age": 32,
        "department": "Neurology",
        "admitted": False
    },
    {
        "id": 3,
        "name": "Hari",
        "age": 45,
        "department": "Cardiology",
        "admitted": True
    },
    {
        "id": 4,
        "name": "Gita",
        "age": 29,
        "department": "Orthopedic",
        "admitted": True
    }
]


@app.get("/patients")
def get_patients(department: Optional[str] =None,  admitted:Optional[bool] =None) : 
    filtered_patients = patients   
    if department : 
        filtered_patients = [  
            p for p in filtered_patients   
            if p["department"].lower()   == department.lower()   
        ]

    if admitted is not None :
        filtered_patients  = [  
            p for p in filtered_patients  
            if p.get("admitted")  == admitted 
        ]
    return filtered_patients




@app.get("/patients/{patient_id}")
def get_patient_by_id (patient_id : Optional[int] = None) : 
    for i  in patients : 
        if i["id"]  == patient_id : 
            return i  
    return {
    "message": "Patient not found"
     }


@app.post("/patients")   
def add_patient (patient:Patient) : 
    new_id = len(patients) + 1    
    new_patient  = patient.model_dump()
    new_patient["id"]  = new_id  
    patients.append(new_patient)
    return  new_patient  

'''




'''
from fastapi import FastAPI  
from typing import Optional  
from pydantic import BaseModel  


app = FastAPI ( )

class Order(BaseModel) : 
    customer: str   
    product:str 
    category :str  
    price :float  
    status :str


orders = [
    {
        "id": 1,
        "customer": "Ram",
        "product": "Laptop",
        "category": "Electronics",
        "price": 80000,
        "status": "Delivered"
    },
    {
        "id": 2,
        "customer": "Sita",
        "product": "Shoes",
        "category": "Fashion",
        "price": 5000,
        "status": "Pending"
    },
    {
        "id": 3,
        "customer": "Hari",
        "product": "Mobile",
        "category": "Electronics",
        "price": 50000,
        "status": "Delivered"
    },
    {
        "id": 4,
        "customer": "Gita",
        "product": "Bag",
        "category": "Fashion",
        "price": 3000,
        "status": "Cancelled"
    }
]




@app.get("/orders")
def get_orders(customer :Optional[str] = None, category:Optional[str] = None, status:Optional[str] =None) : 
    filtered_orders  = orders  
    if customer : 
        filtered_orders  = [  
            o for o  in filtered_orders  
            if o["customer"].lower()  == customer.lower()
        ]

    if category : 
        filtered_orders = [  
            o  for o in filtered_orders  
            if o["category"].lower() == category.lower()
        ]

    if status : 
        filtered_orders=  [ 
             o for o  in filtered_orders  
             if o["status"].lower() == status.lower()
        ]
    return filtered_orders



@app.post("/orders")
def add_order(order:Order) : 
    new_id  = len(orders) + 1  
    new_order = order.model_dump()
    new_order["id"]  = new_id  
    orders.append(new_order)
    return  { 
        "message":"Order created successfully" , 
        "data"  : new_order
    }

@app.get("/orders/customer/{customer_name}")
def get_orders_by_customer(customer_name:str) : 
    filtered_orders = [ 
        o for o in orders   
        if o["customer"].lower() == customer_name.lower()
    ]
    return filtered_orders

@app.get("/orders/{order_id}")
def get_order_by_id (order_id:int) : 
    for i in orders : 
        if i ["id"] == order_id  : 
            return i  
    return   { 
        "message" : "Order not found"
    }

'''



'''
from fastapi import FastAPI  ,HTTPException
from typing import Optional  
from pydantic import BaseModel  

app  = FastAPI()

class CreateBook(BaseModel) : 
    title:str  
    author : str   
    category :str  
    available:bool

books = [
  {"id": 1, "title": "Python Basics", "author": "Ram", "category": "Programming", "available": True},
  {"id": 2, "title": "Data Science", "author": "Sita", "category": "Programming", "available": False},
  {"id": 3, "title": "English Grammar", "author": "Hari", "category": "Education", "available": True},
  {"id": 4, "title": "Machine Learning", "author": "Ram", "category": "Programming", "available": True}

]

@app.get("/books")   
def get_books () :   
    if not books : 
        return  {"Not Book found" :[]}
    return books



@app.get("/books/filter")
def get_book_byquerry(category: Optional[str] = None, available: Optional[bool] = None): 
    filtered_books = books  

    if category is not None : 
        filtered_books = [b for b in filtered_books if b["category"].lower() == category.lower()]

    if available is not None :  
        filtered_books  = [b for b in filtered_books   if b["available"] == available ]

    if not filtered_books : 
        raise HTTPException ( 
            status_code=404 ,  
            detail= "No books found matching the criteria"
        )

    return filtered_books

    

@app.get("/books/{book_id}")
def get_bookby_id (book_id : int ) : 
    for book in books : 
        if book["id"]  == book_id : 
            return book    

    raise HTTPException(status_code=404 , detail="Book not found")



@app.post("/books")
def create_new_books(book:CreateBook) : 
    if book.title.strip() == ""  or book.author.strip() == "" or book.category.strip() == "": 
        raise HTTPException(
            status_code=400 , 
            detail= { 
                "message1" : "please ensure that the book title  , book category and book author must be provided not white space",
                "message2" : "please make sure when you write you cannot give the space in first "

            }
        )

    if books : 
        new_id   = books[-1]["id"] + 1 
    else  : 
        new_id = 1 

    new_book   = book.model_dump()
    new_book["id"]  = new_id
    books.append(new_book)
    return new_book
    
'''



'''
from fastapi import FastAPI  ,HTTPException  
from typing import Optional  
from pydantic import BaseModel  

app  = FastAPI ( )  

class SubmitAccount (BaseModel) : 
    name : str   
    balance :float  
    account_type: str   
    active : bool

accounts = [
    {"id": 1, "name": "Ram", "balance": 50000, "account_type": "Saving", "active": True},
    {"id": 2, "name": "Sita", "balance": 25000, "account_type": "Current", "active": True},
    {"id": 3, "name": "Hari", "balance": 0, "account_type": "Saving", "active": False},
    {"id": 4, "name": "Gita", "balance": 80000, "account_type": "Saving", "active": True}
]




@app.get("/accounts")
def get_accounts  () : 
    if not accounts : 
        raise HTTPException ( 
            status_code=404 ,   
            detail= "Account not Found"
        )
    return accounts


@app.get("/accounts/filter")  
def get_account_by_querry (name:Optional[str] =None  , account_type :Optional[str] =None , active:Optional[bool] = None) : 
    filtered_accounts   =  accounts  

    if name is not None  : 
        filtered_accounts  = [
            n for n  in filtered_accounts 
            if n["name"].lower() == name.lower()
        ]
    if account_type is not None : 
        filtered_accounts  = [
            at for at in filtered_accounts    
            if at["account_type"].lower()  == account_type.lower()
        ]  

    if active is not None    : 
        filtered_accounts   = [  
            b for b  in filtered_accounts  
            if b["active"]  == active
        ]

    if not filtered_accounts : 
        raise HTTPException  ( 
            status_code=404 , 
            detail="No account found"
        )
    
    return filtered_accounts
    



@app.get("/accounts/{account_id}")
def get_account_by_id (account_id :int) : 
    for   id in accounts : 
        if id["id"] == account_id : 
            return id  
    raise HTTPException ( 
        status_code=404 ,  
        detail="Account not found"
    )

@app.post("/accounts")
def post_account (account:SubmitAccount) : 
    if account.name.strip() == "" : 
        raise HTTPException  ( 
            status_code=400  , 
            detail= "please fill the form dont leave white space"
        )
    if account.balance  < 0 : 
        raise HTTPException ( 
            status_code=400 , 
            detail="The account balance most be positive number"
        )

    if accounts : 
        new_id  = accounts[-1]["id"]+1  
    else : 
        new_id =  1 

    new_account = account.model_dump()
    new_account["id"] = new_id  
    accounts.append(new_account)
    return new_account
'''



""" 
from fastapi import FastAPI   ,HTTPException
from typing import Optional  
from pydantic import BaseModel  

app  = FastAPI()
class CreateBooking(BaseModel ) : 
    guest : str  
    room:int      
    days:int   
    status : str 

bookings = [
    {
        "id": 1,
        "guest": "Ram",
        "room": 101,
        "days": 3,
        "status": "Booked"
    },
    {
        "id": 2,
        "guest": "Sita",
        "room": 102,
        "days": 2,
        "status": "Cancelled"
    },
    {
        "id": 3,
        "guest": "Hari",
        "room": 103,
        "days": 5,
        "status": "Booked"
    }
]


@app.get("/bookings")  
def get_bookings () :    
    if not bookings : 
        raise HTTPException  (  
            status_code= 404  ,  
            detail= "Book not Found "
        )
    return  bookings


@app.get("/bookings/filter")
def get_booking_byQ   (guest:Optional[str] = None , status:Optional[str]  = None)   : 
    filtered_booking  = bookings

    if guest is not None :  
        filtered_booking = [ 
            g for g in filtered_booking   
            if g["guest"].lower()  == guest.lower()
        ]
    if status is not None : 
        filtered_booking = [  
            s for s in filtered_booking   
            if s["status"].lower()  == status.lower()
        ]
    if not filtered_booking  :   
        raise HTTPException  (  
            status_code= 404 , 
            detail= "No booking found"
        )
    return filtered_booking


@app.get("/bookings/{booking_id}")
def get_booking_by_id (booking_id : int)  : 
    for i  in bookings : 
        if i["id"]   == booking_id : 
            return  i    

    raise HTTPException ( 
        status_code=404 , 
        detail= "booking id not Found"
    )

@app.post("/bookings")
def add_bookings (book : CreateBooking) : 
    if book.guest.strip() == "" : 
        raise HTTPException ( 
            status_code=400 , 
            detail="please fill the blank"
        )  

    if book.days <= 0 or book.room  <= 0: 
        raise HTTPException ( 
            status_code=400 , 
            detail= "book day most be positive and greater than 0"
        )

    if book.status != "Booked" and book.status != "Cancelled" : 
        raise  HTTPException ( 
            status_code=400 , 
            detail= "Status must be Booked / Cancelled"
        )

    if bookings  : 
        new_id   = bookings[-1]["id"] +1   
    if not bookings : 
        new_id  = 1   

    new_booking  = book.model_dump()
    new_booking["id"]   = new_id  
    bookings.append(new_booking)
    return new_booking
"""


'''
from fastapi import FastAPI  ,HTTPException 
from pydantic import BaseModel  
from typing import Optional  

app  = FastAPI()
class CreateProduct(BaseModel) : 
    name :str   
    category :str   
    price : float  
    stock :int   


products = [
    {
        "id": 1,
        "name": "Laptop",
        "category": "Electronics",
        "price": 85000,
        "stock": 5
    },
    {
        "id": 2,
        "name": "Mouse",
        "category": "Electronics",
        "price": 1500,
        "stock": 20
    },
    {
        "id": 3,
        "name": "Keyboard",
        "category": "Electronics",
        "price": 3000,
        "stock": 0
    },
    {
        "id": 4,
        "name": "Notebook",
        "category": "Stationery",
        "price": 200,
        "stock": 50
    }
]


@app.get("/products")   
def get_products  ( )  : 
    if not products :  
        raise HTTPException ( 
            status_code=404 ,  
            detail= "Products not found "
        )
    return products


@app.get("/products/filter")
def get_product_by_querry (category :Optional [str] = None , max_price:Optional[float] = None , in_stock : Optional[bool] = None ) : 
    filter_product  = products  

    if category is not None  : 
        filter_product   = [  
            c for c in filter_product   
            if c["category"].lower()  == category.lower()
        ]
    if max_price is not None : 
        filter_product       =  [ 
            p for p  in filter_product   
            if p["price"] <= max_price  
        ]
    if  in_stock is not None : 
        if in_stock :  
            filter_product  = [p for p in filter_product  if p["stock"]  > 0]   
        else  : 
            filter_product = [p for  p in filter_product if p["stock"] == 0 ]  

    if not filter_product : 
        raise HTTPException (  
            status_code= 404 ,  
            detail= "No products matched the filter criteria."
        )
    return filter_product






@app.get("/products/{product_id}")   
def get_products_by_id(product_id :int) : 
    for i  in products : 
        if i["id"]  == product_id  : 
            return i   
    raise HTTPException (  
        status_code= 404 ,  
        detail= f"product id {product_id} not found"
    )


@app.post ("/products")

def post_product (product :CreateProduct) : 
    if product.name.strip () == "" or product.category.strip () == "" : 
        raise HTTPException ( 
            status_code=400 , 
            detail= "Please Do not leave the blank onf name and category ,"
        )
    if product.price <= 0 : 
        raise HTTPException ( 
            status_code=400 , 
            detail= "price must be above 0"

        )

    if product.stock  < 0 : 
        raise HTTPException  ( 
            status_code= 400    , 
            detail= "please ensure thaht stock be positive"
        )
    if products : 
        new_id   = products[-1]["id"]+1 
    else : 
        new_id  = 1   

    new_product  = product.model_dump()
    new_product["id"]  = new_id  
    products.append(new_product)
    return new_product

'''



'''
from typing import Optional
from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, Field

app = FastAPI()

inventory = [
    {"id": 101, "title": "Wireless Mouse", "category": "Electronics", "price": 1200.0, "stock": 15, "discount": 10.0},
    {"id": 102, "title": "Mechanical Keyboard", "category": "Electronics", "price": 4500.0, "stock": 0, "discount": 0.0},
    {"id": 103, "title": "Python Programming Book", "category": "Books", "price": 850.0, "stock": 30, "discount": 5.0},
    {"id": 104, "title": "Gaming Monitor", "category": "Electronics", "price": 25000.0, "stock": 4, "discount": 15.0},
]


# 1. Request Body Schema
class ItemCreate(BaseModel):
    title: str = Field(..., min_length=3)
    category: str = Field(..., min_length=1)
    price: float = Field(..., gt=0)
    stock: int = Field(..., ge=0)
    discount: float = Field(0.0, ge=0.0, le=50.0)


# 2. Response Schema
class ItemResponse(BaseModel):
    id: int
    title: str
    category: str
    price: float
    final_price: float
    stock: int


# POST Endpoint
@app.post("/items", response_model=ItemResponse, status_code=status.HTTP_201_CREATED)
def create_item(item: ItemCreate):
    new_id = max((i["id"] for i in inventory), default=100) + 1
    calculated_final_price = item.price - (item.price * item.discount / 100.0)

    new_item = {
        "id": new_id,
        "title": item.title,
        "category": item.category,
        "price": item.price,
        "final_price": calculated_final_price,
        "stock": item.stock,
        "discount": item.discount
    }
    
    inventory.append(new_item)
    return new_item


# PUT Endpoint
@app.put("/items/{item_id}", response_model=ItemResponse)
def update_item(item_id: int, item: ItemCreate):
    for i in inventory:
        if i["id"] == item_id:
            calculated_final_price = item.price - (item.price * item.discount / 100.0)
            
            i["title"] = item.title
            i["category"] = item.category
            i["price"] = item.price
            i["stock"] = item.stock
            i["discount"] = item.discount
            i["final_price"] = calculated_final_price
            
            return i

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Item with ID {item_id} not found"
    )


# DELETE Endpoint
@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    for index, item in enumerate(inventory):
        if item["id"] == item_id:
            inventory.pop(index)
            return {"message": "Item deleted successfully"}

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Item with ID {item_id} not found"
    )
'''  




'''IMPORTANT 
from fastapi import FastAPI  ,HTTPException 
from pydantic import BaseModel  
from  typing import Optional  


app  = FastAPI ()

class CreateStudent(BaseModel) : 
    name : str   
    age : int  
    course : str   
    active :bool 

class UpdateStudent(BaseModel) : 
    name : Optional[str]    = None  
    age : Optional[int]  = None  
    course : Optional[str]  = None  
    active : Optional[bool] = None  

students = [
    {
        "id": 1,
        "name": "Ram",
        "age": 20,
        "course": "Python",
        "active": True
    },
    {
        "id": 2,
        "name": "Sita",
        "age": 21,
        "course": "Data Science",
        "active": True
    },
    {
        "id": 3,
        "name": "Hari",
        "age": 19,
        "course": "Python",
        "active": False
    }
]


@app.get("/students")
def get_stuents   () : 
    if not students : 
        raise  HTTPException ( 
            status_code= 404 , 
            detail= "Student not found"
        )
    return  students


@app.get("/students/filter")
def get_student_by_q (course:Optional[str] = None , active:Optional[bool] = None)   : 
    filtered_student  = students  

    if course is not None : 
        filtered_student   = [  
            c for c in filtered_student   
            if c["course"].lower()  == course.lower()
        ]
    if active is not None : 
        filtered_student  = [ 
            a for a in filtered_student  
            if a["active"]  == active 
        ]

    if not filtered_student : 
        raise HTTPException ( 
            status_code=404 ,  
            detail= " no student found"
        )
    return filtered_student

@app.get("/students/{student_id}")
def get_student_by_id (student_id :int) : 
    for   student in students :  
        if student["id"]  == student_id : 
            return student  
    raise HTTPException ( 
        status_code= 404 , 
        detail= f"student  with id {student_id} not found"
    )

@app.post("/students")
def post_student (student : CreateStudent ,) : 
    if student.name.strip()  == "" : 
        raise HTTPException ( 
            status_code= 400 , 
            detail= "Please fill the name"
        )

    if student.age <= 0 : 
        raise HTTPException ( 
            status_code= 400  , 
            detail= "Please ensure that the age is most be greater than 0"
        )   

    if students : 
        new_id  = students[-1]["id"]+1  
    else :
        new_id  = 1   

    new_student  = student.model_dump()
    new_student["id"]  = new_id  
    students.append(new_student)
    return new_student

@app.put("/students/{student_id}")
def change_data(student_id: int, student_details: CreateStudent):
    if student_details.name.strip() == "" : 
        raise HTTPException ( 
            status_code= 400 , 
            detail= "Ensure that the  name must be not whitespace"
        )  

    if  student_details.age <= 0 : 
        raise HTTPException ( 
            status_code= 400 , 
            detail   = "age must be positive and above the 0"
        )
    
    for index,student  in enumerate (students) : 
        if student["id"]   == student_id : 
            change_detail   = student_details.model_dump()
            change_detail["id"]  = student_id  
            students[index]  = change_detail  
            return  change_detail

    raise HTTPException(
        status_code=404,
        detail=f"student with ID {student_id} not found"
    )

    

@app.delete("/students/{student_id}")
def delete_student(student_id: int):
    for index, student in enumerate(students):
        if student["id"] == student_id:
            del students[index]
            return {"message": f"student with ID {student_id} deleted"}

    raise HTTPException(
        status_code=404,
        detail=f"student with ID {student_id} not found"
    )


@app.patch("/students/{student_id}")
def update_student_partial(student_id: int, student_updates: UpdateStudent):
    for index, student in enumerate(students):
        if student["id"] == student_id:
            updated_student = student.copy()

            if student_updates.name is not None:
                if student_updates.name.strip() == "":
                    raise HTTPException(
                        status_code=400,
                        detail="Ensure that the name must not be whitespace"
                    )
                updated_student["name"] = student_updates.name

            if student_updates.age is not None:
                if student_updates.age <= 0:
                    raise HTTPException(
                        status_code=400,
                        detail="age must be positive and above 0"
                    )
                updated_student["age"] = student_updates.age

            if student_updates.course is not None:
                updated_student["course"] = student_updates.course

            if student_updates.active is not None:
                updated_student["active"] = student_updates.active

            students[index] = updated_student
            return updated_student

    raise HTTPException(
        status_code=404,
        detail=f"student with ID {student_id} not found"
    )
'''



'''
from fastapi import FastAPI    , HTTPException
from typing import Optional  
from pydantic import BaseModel  

app  = FastAPI ()

class CreateEmployee(BaseModel) : 
    name : str  
    department:str  
    salary :  float  
    active: bool 


class EmployeeUpdate(BaseModel) : 
    name  : Optional[str] = None  
    department : Optional[str] = None  
    salary : Optional[float]  = None  
    active : Optional[bool] = None


employees = [
    {
        "id": 1,
        "name": "Ram",
        "department": "IT",
        "salary": 50000,
        "active": True
    },
    {
        "id": 2,
        "name": "Sita",
        "department": "HR",
        "salary": 45000,
        "active": True
    },
    {
        "id": 3,
        "name": "Hari",
        "department": "IT",
        "salary": 60000,
        "active": False
    }
]


@app.get("/employees")
def get_employee  () : 
    if not employees :   
        HTTPException ( 
            status_code= 404,  
            detail="Employees Not found"
        )
    return employees  



@app.get("/employees/filter")
def get_employee_by_querry (department:Optional[str]  = None , active : Optional[bool]  = None)  :    
    filtered_employees = employees    

    if department is not None : 
        filtered_employees  = [ 
            d for d in filtered_employees   
            if d["department"].lower()  == department.lower()
        ]   
    if active is not None : 
        filtered_employees  = [  
            a for a in filtered_employees  
            if a["active"] == active
        ]    

    if not filtered_employees : 
        raise  HTTPException (  
            status_code= 404 , 
            detail= " Student not Found"
        )
    return filtered_employees


@app.get("/employees/{employee_id}")
def get_employee_by_id (employee_id :int) : 
    for emp in employees   : 
        if emp["id"]  == employee_id : 
            return emp  
        
    raise  HTTPException ( 
        status_code= 404 ,  
        detail= f"With id {employee_id} not found"
    )


@app.post ("/employees")
def create_employee (detail : CreateEmployee) : 
    if detail.name.strip()  == ""  or detail.department.strip()  == "": 
        raise HTTPException ( 
            status_code= 400 ,  
            detail = "Donot leave the blank on name or department" , 
            
        )

    if detail.salary <= 0 : 
        raise HTTPException (  
            status_code=400 , 
            detail="Salary most be positive and above  0 "
        )

    if employees : 
        new_id  = employees[-1]["id"] +1   
    else : 
        new_id  = 1   

    new_employee = detail.model_dump()  
    new_employee["id"]   = new_id  
    employees.append(new_employee)
    return  new_employee 



@app.put("/employees/{employee_id}")   
def change_data (employee_id :int  , detail  : CreateEmployee) : 

    for index,emp in enumerate(employees) : 
        if emp["id"]  == employee_id : 
            change   = detail.model_dump()
            change["id"]   = employee_id   
            employees[index]   =  change  
            return change    

    raise  HTTPException ( 
        status_code= 404 ,  
        detail= f"with id {employee_id} not found"
    )


@app.delete("/employees/{employee_id}")
def delete_employee (employee_id  : int)  :  
    for   index, emp in enumerate (employees) : 
        if emp["id"]   == employee_id : 
            del employees[index]
            return  {
                "message" : f"employee id {employee_id} information delete "  , 
                "details" : emp
            }
    raise HTTPException (  
        status_code= 404 , 
        detail= f"with id {employee_id } not found"
    )


@app.patch("/employees/{employee_id}")
def update_data (employee_id : int  , data : EmployeeUpdate) : 
    for emp  in employees : 
        if emp["id"]   == employee_id  : 
            stored_data  = data.model_dump(exclude_unset=True)   
            emp.update(stored_data)
            return {"message": "Employee updated successfully", "employee": emp}
    raise HTTPException (
        status_code=404 , 
        detail= "employee not found"
    )
'''




'''
from fastapi import FastAPI  ,HTTPException
from typing import Optional  
from pydantic  import BaseModel  

app  = FastAPI()  

class CreateOrders(BaseModel) : 
    customer : str  
    item : str
    category : str  
    quantity : int   
    price : float  
    status  : str  

class Change(BaseModel) : 
    customer :Optional[str] =None  
    item:Optional[str] = None  
    category :Optional[str] = None 
    quantity : Optional[int] = None  
    price : Optional[float] = None  
    status  : Optional[str] = None

orders = [
    {
        "id": 1,
        "customer": "Amit",
        "item": "Pizza",
        "category": "Fast Food",
        "quantity": 2,
        "price": 1200,
        "status": "Preparing"
    },
    {
        "id": 2,
        "customer": "Nisha",
        "item": "Momo",
        "category": "Snacks",
        "quantity": 3,
        "price": 450,
        "status": "Delivered"
    },
    {
        "id": 3,
        "customer": "Bikash",
        "item": "Burger",
        "category": "Fast Food",
        "quantity": 1,
        "price": 350,
        "status": "Pending"
    },
    {
        "id": 4,
        "customer": "Riya",
        "item": "Chowmein",
        "category": "Chinese",
        "quantity": 2,
        "price": 500,
        "status": "Preparing"
    }
]


@app.get("/orders")
def get_orders () : 
    if not orders : 
        raise HTTPException ( 
            status_code= 404 , 
            detail= "Orders Not found"
        )
    return orders


@app.get("/orders/filter")
def get_order_by_filter(customer :Optional[str] =None , category:Optional[str] = None , status:Optional[str] = None) : 
    filtered_orders = orders  

    if customer is not None : 
        filtered_orders = [ 
            c  for c in filtered_orders  
            if c["customer"].lower()  == customer.lower()
        ]

    if category is not None : 
        filtered_orders  =[ 
            c for c in filtered_orders   
            if c["category"].lower()  == category.lower()
        ]

    if status is not None : 
        filtered_orders  = [ 
            s for s in filtered_orders  
            if s["status"].lower()  == status.lower()
        ]  

    if not filtered_orders : 
        raise HTTPException ( 
            status_code= 404 , 
            detail= "orders not found"
        )
    return filtered_orders




@app.get("/orders/{order_id}")
def get_orders_by_id (order_id :int)  : 
    for order in orders : 
        if order["id"]  == order_id : 
            return order
        
    raise HTTPException ( 
        status_code=404 , 
        detail= f"with orders id {order_id} not found"
    )


@app.post ("/orders")
def post (create: CreateOrders) : 
    if create.customer.strip() == "" : 
        raise HTTPException ( 
            status_code=400 , 
            detail="please fill the customer"
        )
    if create.item.strip() =="" : 
        raise HTTPException ( 
            status_code= 400 , 
            detail= "Please fill the item"
        )
    if create.quantity <= 0 : 
        raise HTTPException ( 
            status_code= 400 , 
            detail= "Please insure that quantity must be above 0"
        )  

    if create.price <=0  : 
        raise HTTPException ( 
            status_code= 400 , 
            detail= "please insure that quantity must be above 0"
        )

    if create.status not in ["pending","preparing","delivered"] : 
        raise HTTPException ( 
            status_code= 400 , 
            detail="Only fill the pending/preparing and delivered"
        )

    if orders : 
        new_id  = orders[-1]["id"]+1  
    else : 
        new_id = 1   

    new_orders  = create.model_dump()
    new_orders["id"]  = new_id  
    orders.append(new_orders)
    return new_orders


@app.put("/orders/{order_id}")  
def put (order_id :int , all_change: CreateOrders) : 
    for index,order in enumerate(orders) : 
        if order["id"] == order_id : 
            change  = all_change.model_dump()
            change["id"]    = order_id   
            orders[index]  = change  
            return change  

    raise HTTPException ( 
        status_code= 404 ,  
        detail= f"with id {order_id} not found"
    )


@app.patch ("/orders/{order_id}")
def patch (order_id :int ,  update:Change) : 
    for order in orders : 
        if order["id"] == order_id : 
            update_data = update.model_dump(exclude_unset=True)
            order.update(update_data)
            return update_data  
    raise HTTPException ( 
        status_code= 404 , 
        detail=f"with id {order_id} not found"
    )

@app.delete("/orders/{order_id}")
def delete (order_id : int)  : 
    for index,order  in enumerate(orders) : 
        if order["id"]  == order_id : 
            del orders[index]    
            return { 
                "message" :f"id with {order_id} orders delete"
            }
    raise HTTPException( 
        status_code= 404 , 
        detail= "not found"
    )
'''


from fastapi import FastAPI  ,HTTPException
from typing import Optional  
from pydantic import BaseModel  


app =  FastAPI()

class CreateRental(BaseModel) : 
    customer:str
    vehicle:str
    vehicle_type:str
    days:int
    daily_rate:float
    returned:bool


rentals = [
    {
        "id": 1,
        "customer": "Anil",
        "vehicle": "Toyota Corolla",
        "vehicle_type": "Car",
        "days": 4,
        "daily_rate": 2500,
        "returned": False
    },
    {
        "id": 2,
        "customer": "Mina",
        "vehicle": "Honda Dio",
        "vehicle_type": "Bike",
        "days": 2,
        "daily_rate": 800,
        "returned": True
    },
    {
        "id": 3,
        "customer": "Kiran",
        "vehicle": "Mahindra Scorpio",
        "vehicle_type": "SUV",
        "days": 6,
        "daily_rate": 4000,
        "returned": False
    },
    {
        "id": 4,
        "customer": "Puja",
        "vehicle": "Yamaha FZ",
        "vehicle_type": "Bike",
        "days": 3,
        "daily_rate": 1200,
        "returned": False
    }
]


@app.get("/rentals")
def get_rentals () : 
    if not rentals :   
        raise HTTPException ( 
            status_code= 404 ,  
            detail= "rentals not found"
        )
    return rentals 


@app.get("/rentals/filter")
def get_rental_by_querry (customer:Optional[str] = None , vehicle_type:Optional[str] = None, returned:Optional[bool] = None) :
    filtered_rental = rentals  
    if customer is not None : 
        filtered_rental  = [ 
            c for c in  filtered_rental  
            if c["customer"].lower()  == customer.lower()
        ]

    if vehicle_type is not None : 
        filtered_rental  = [ 
            v for v in filtered_rental  
            if v["vehicle_type"].lower()  == vehicle_type.lower()
        ]

    if returned is not None : 
        filtered_rental   = [ 
            r for r in filtered_rental  
            if r["returned"]  == returned
        ]
    if not filtered_rental : 
        raise HTTPException ( 
            status_code= 404 , 
            detail= "Not filtered rentals"
        )

    return filtered_rental




@app.get("/rentals/{rental_id}")
def get_rental_by_id(rental_id :int) : 
    for rental in rentals : 
        if rental["id"] ==rental_id : 
            return rental    
    raise HTTPException ( 
        status_code= 404 , 
        detail= f"With ID {rental_id} not found"
    )

@app.post("/rentals")
def create_rentals(create :CreateRental) : 
    if create.customer.strip()  =="" : 
        raise HTTPException ( 
            status_code= 400  , 
            detail= "Please fill the customer option"
        )

    if create.vehicle.strip() =="" : 
        raise HTTPException ( 
            status_code= 400 , 
            detail="Please fill the vehicle option"
        )

    if create.days <= 0 : 
        raise HTTPException ( 
            status_code= 400   , 
            detail="Please days must be above then 0"
        )
    if create.daily_rate <=0 : 
        raise HTTPException ( 
            status_code= 400 , 
            detail="Ensure that the daily rate be above 0"
        )
    if create.vehicle_type not in ["Car","Bike","Suv"] : 
        raise HTTPException ( 
            status_code= 400 , 
            detail="Vehicle type must be Car/Bike/Suv"
        )

    if rentals : 
        new_id = rentals[-1]["id"]+1  
    else : 
        new_id = 1  

    new_rental  = create.model_dump()
    new_rental["id"] = new_id  
    rentals.append(new_rental)
    return new_rental