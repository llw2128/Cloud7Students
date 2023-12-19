from fastapi import FastAPI, Response, Request
from pydantic import BaseModel
from fastapi_pagination import LimitOffsetPage, add_pagination, paginate
from fastapi_pagination.links import Page
import json
from strawberry.asgi import GraphQL
import strawberry
import typing
from datetime import datetime

# Launch directly and not use the standard FastAPI startup
import uvicorn

from resources.students import StudentsResource

app = FastAPI()
add_pagination(app)

@strawberry.type
class StudentType:
    uni: str
    first_name: str
    last_name: str
    email: str
    school: str
    year: int

def getStudentTypes(root) -> typing.List[StudentType]:
    allStudentTypes = []
    all_students = students_resource.get_students()
    for student in all_students:
        allStudentTypes.append(StudentType(uni=student["uni"],
                           first_name=student["first_name"], 
                           last_name=student["last_name"], 
                           email=student["email"],
                           school=student["school"],
                           year=int(student["year"])))
    
    return allStudentTypes

@strawberry.type
class Query:
    student: typing.List["StudentType"] = strawberry.field(resolver=getStudentTypes)

schema = strawberry.Schema(query=Query)
graphql_app = GraphQL(schema)

students_resource = StudentsResource()

class Student(BaseModel):
    uni: str
    first_name: str
    last_name: str
    email: str
    school: str
    year: int

app.add_route("/graphql", graphql_app)
app.add_websocket_route("/graphql", graphql_app)

@app.middleware('http')
async def log_request_details(request: Request, call_next):
    method_name = request.method
    path = request.url.path
    start_time = datetime.now()
    response = await call_next(request)
    process_time = datetime.now() - start_time
    with open('request_log.txt', mode='a') as file:
        content = f"Request: {method_name} {path}, Received at: {start_time.strftime('%Y-%m-%d %H:%M:%S')}, Process time: {process_time}s \n"
        file.write(content)

    return response

@app.get("/")
async def root():
    return {"message": "This is the brand new Cloud7 students microservice deployed on EC2!"}

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
async def get_students() -> Page[Student]:
    all_students = students_resource.get_students()
    paginated_students = paginate(all_students)

    return paginated_students

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

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8012)
