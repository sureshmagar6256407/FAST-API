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


from fastapi import FastAPI  
app  = FastAPI()

@app.get("/products")
def mobile_details (category:str, min_price:int): 
    return { 
        "category" : category   , 
        "min_price" : min_price
    }


