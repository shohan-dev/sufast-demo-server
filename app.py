from sufast import App

app = App()

@app.get("/")
def hello():
    return {"message": "Hello from Sufast 👋"}
@app.get("/shohan")
def hello():
    return {"message": "Hello from shohan Buddy 👋"}

app.run() 