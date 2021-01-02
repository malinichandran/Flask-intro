from flask import Flask, request
from operations import add,sub,mult,div
app= Flask(__name__)



@app.route('/add')
def add_opera():
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = add(a, b)
    return f"<p>The result is {result}</p>"

@app.route('/sub')
def sub_opera():
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = sub(a,b)
    return f"<p>The result is {result}</p>"

@app.route('/mul')
def mul_opera():
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = mult(a,b)
    return f"<p>The result is {result}</p>"

@app.route('/div')
def div_opera():
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = div(a,b)
    return f"<p>The result is {result}</p>"