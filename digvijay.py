from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel
from scrapy import Item

app = FastAPI()
class Employee(BaseModel):
    name :str
    role :str
employee = {

    1: {
        "name":"digvijay",
        "role":"tester"

    }
}

@app.get("/test/{employee_id}")
def test(employee_id:int):
    if employee_id in employee:
        return employee[employee_id]
    return {"error": "details not found"}


@app.get("/query/{employe_id}")
def get_by_query(employe_id:int, name:str):
    for employe_id in employee:
        if employee[employe_id]["name"] == name:
            return employee[employe_id]
    return {"data":"not found"}

@app.post("/post/{employe_id}")
def create(employe_id: int, employe: Employee):
    if employe_id in employee:
        return {"Employee": "ID already exists"}
    employee[employe_id] = employe
    return employee[employe_id]

@app.put("/update/{employe_id}")
def update(employe_id:int, employe:Employee):
    if employe_id not in employee:
        return {"Employe":"NOt exsists"}
    employee[employe_id] = employe
    
@app.delete("/delete/{employee_id}")
def delete(employee_id:int):
    if employee_id not in employee:
        return {"Error":"Student doesn't exists"}
    del employee[employee_id]
    return {"Student":"Deleted"}


#@app.get("/items/{item_id}")
#def read_item(item_id: int, q: Union[str, None] = None):
 #   return {"item_id": item_id, "q": q}

