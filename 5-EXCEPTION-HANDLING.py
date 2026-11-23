from fastapi import FastAPI  , HTTPException  
from pydantic import BaseModel 
app  = FastAPI ( )

class MarksSubmission(BaseModel) :  
    student_id : str  
    marks : int  
    subject:str


students = {  
    "S101" : {"name":"suresh pun " ,"age":20  ,"grade":"A+" ,"marks" : 90},
     "S102" : {"name":"Tekam oli " ,"age":22  ,"grade":"A","marks":85},
      "S103" : {"name":"rahul budha " ,"age":19 ,"grade":"B","marks":70},
       "S104" : {"name":"himal kc " ,"age":17  ,"grade":"C+","marks":67},
        "S105" : {"name":"bijaya bk " ,"age":21  ,"grade":"B+","marks":69},
}

@app.get("/student/{student_id}")
def get_student_by_id (student_id : str) : 
    if student_id not in students: 
        raise HTTPException ( 
            status_code=404,
            detail=f"the student ID {student_id} does not exist"
        )
    return students[student_id]


@app.post("/submit-marks")
def submit_marks (submission:MarksSubmission) :    
    if submission.student_id not in students : 
        raise HTTPException ( 
            status_code=404   , 
            detail= f"student with id : {submission.student_id} does not exist"
        )
     
    if submission.marks < 0 or submission.marks > 100 : 
        raise HTTPException ( 
            status_code=400  , 
            detail= { 
                "error" : "marks between o and 100"
                , "marks_receive" : submission.marks ,   
                "fix" :"Enter a valid valud between 0 and 100"
            }
        )
    if submission.subject.strip() =="" : 
        raise HTTPException ( 
            status_code=400 ,  
            detail= "subject name cannot be empyt"
        )
    students[submission.student_id]["marks"]  = submission.marks
    return { 
        "message" : "marks submitted successfully" , 
        "student" : students[submission.student_id]["name"] , 
        "subject" :submission.subject  , 
        "marks":submission.marks,
        "age":students[submission.student_id]["age"]
    }
