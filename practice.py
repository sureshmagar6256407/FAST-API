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



from fastapi import FastAPI 
from pydantic import BaseModel  
from typing import Optional 

app  = FastAPI()

class CreateEmployees(BaseModel):     
    name:str  
    department:str 
    salary:float

employees = [
    {"id": 1, "name": "Ram", "department": "IT", "salary": 50000},
    {"id": 2, "name": "Sita", "department": "HR", "salary": 45000},
    {"id": 3, "name": "Hari", "department": "IT", "salary": 60000}
]

@app.get("/employees")
def get_byQu   (department:Optional[str] |None =None) : 
    if not department : 
        return employees 

    filtered_dep  = [de for de in employees if department.lower() == de["department"].lower()]
    return filtered_dep

@app.get("/employees/{employee_id}")
def get_bypath   (employee_id :int) : 
    for i  in employees : 
        if i["id"]  == employee_id : 
            return i 
    return {"message" : "no employee id has in"}

@app.post("/employees")
def create_employee(employee:CreateEmployees) : 
    new_id  = len(employees) + 1  
    new_emplyee = employee.model_dump ()
    new_emplyee["id"]  = new_id  
    employees.append(new_emplyee)
    return { 
        "status" : "the student added"  ,
        "data" : new_emplyee
    }