from fastapi import FastAPI
app = FastAPI()

@app.get("/") #defines the static route
def root():
    return {'message':'Hello world'}

@app.get('/about')
def about():
    return {'message':'New Message'}