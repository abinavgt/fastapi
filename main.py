from fastapi import FastAPI, HTTPException
app = FastAPI()

@app.get("/") #defines the static route
def root():
    return {'message':'Hello world'}

@app.get('/about')
def about():
    return {'message':'New Message'}



@app.get("/items/{id}")  #Dynamic route
def get_items(id: int):
    items = ["Keyboard", "Mouse", "Monitor","CPU"]

    if id < 0 or id >= len(items):
        raise HTTPException(status_code=404, detail = "item not found in doc")
    return items[id]