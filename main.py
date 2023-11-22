from fastapi import FastAPI, Response
from pydantic import BaseModel
from fastapi_pagination import LimitOffsetPage, add_pagination, paginate
import json

# I like to launch directly and not use the standard FastAPI startup
import uvicorn

from resources.students import StudentsResource

app = FastAPI()
add_pagination(app)

students_resource = StudentsResource()

class Student(BaseModel):
    uni: str
    first_name: str
    last_name: str
    email: str
    school: str
    year: int

@app.get("/")
async def root():
    return {"message": "This is the Cloud7 students microservice deployed on EC2!"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Awesome cloud developer amn2211 says hello {name}"}


@app.get("/hello_text/{name}")
async def say_hello_text(name: str):
    the_message = f"Awesome cloud developer amn2211 says Hello {name}"
    rsp = Response(content=the_message, media_type="text/plain")
    return rsp

# /api/students/
# GET all students
# Referenced https://uriyyo-fastapi-pagination.netlify.app/tutorials/limit-offset-pagination/
# to support pagination for this page
@app.get("/students/")
async def get_students() -> LimitOffsetPage[Student]:
    all_students = students_resource.get_students()
    return paginate(all_students)

# /api/students/{uni}
# GET specific student by UNI
@app.get("/students/{uni}")
async def get_students(uni):
    data = students_resource.get_specific_student(uni)
    return data

# /api/students/put/{uni}
# PUT request for student by UNI
@app.put("/students/{uni}", response_model=Student)
async def put_student(uni: str, student: Student):
    return students_resource.put_student(uni, student)

# /api/students/{uni}
# POST request to update student information
@app.post("/students/{uni}", response_model=Student)
async def post_student(uni: str, student: Student):
    return students_resource.post_student(uni, student)

# /api/students/{uni}
# DELETE request for student by uni
@app.delete("/students/{uni}")
async def delete_student(uni):
    return students_resource.delete_student(uni)

# /api/students/{uni}/bookings
# In the future, add api for bookings for a student specified by the UNI

# /api/students/{uni}/banned-spaces
# In the future, add banned spaces for a student specified by the UNI



if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8012)
