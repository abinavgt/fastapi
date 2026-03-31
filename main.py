from fastapi import FastAPI, HTTPException
import json
app = FastAPI()

def load_data():
    with open('patients.json') as f:
        data = json.load(f)
    return data

@app.get("/")  # static route
def root():
    return {'message':'Patient Management API'}

@app.get('/about')
def about():
    return {'message':'A fully functional API to manage your patient records'}



# @app.get("/items/{id}")  #Dynamic route
# def get_items(id: int):
#     items = ["Keyboard", "Mouse", "Monitor","CPU"]

#     if id < 0 or id >= len(items):
#         raise HTTPException(status_code=404, detail = "item not found in doc") 
#     return items[id]

@app.get('view')
def view():
    data = load_data()
    return data
    