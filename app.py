from flask import Flask, jsonify, render_template, request
import json


app = Flask(__name__)
jData = json.loads(open('./challans.json').read())
data=jData["Challans"]

# Intial request Ex: http://192.168.99.100:5000/
@app.route('/')
def route_main():
    return "Welcome! Get challans list in /getchallans/!"

# Returns JSON which containes all airlines
@app.route('/getchallans/')
def airlines_all():
    return render_template("index.html",items=data)

# Returns airlines JSON which matches the id
@app.route('/getchallans/<string:id>/')
def restaurants_by_id(id=''):
    myList=[]
    for element in data:
        if element["id"] == id:
            myList.append(element)
    return render_template("index.html",items=myList)

# Returns the airlines JSON with particualr type
@app.route('/getchallans/car/<string:car>/')
def airlines_by_type(car=''):
    myList=[]
    for element in data:
        if element["car"].lower() == car.lower():
            myList.append(element)
    return render_template("index.html",items=myList)

if __name__ == '__main__':
    app.run(host='0.0.0.0')
