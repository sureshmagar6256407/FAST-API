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


from fastapi import FastAPI  ,HTTPException  
from typing import Optional  
from pydantic import BaseModel  

app  = FastAPI ( )

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