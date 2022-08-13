from flask import Flask
import json
from data import me

app = Flask(__name__)



@app.get("/")
def home():
    return "Hello from flask"



@app.delete("/test")
def test():
    return "This is just another endpoint"


@app.get("/about")
def about():
    return "Hello Wesley"


###########################################################
############## API PRODUCTS################################



@app.get("/api/test")
def test_api():
    return json.dumps("OK")

# get  /api/ bbout return the me dictionary as json
@app.get("/api/about")
def about_api():
    return json.dumps(me)


app.run(debug=True)