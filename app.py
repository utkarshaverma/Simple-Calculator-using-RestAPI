from flask import Flask, request, render_template
from flask_restful import Api,Resource

app = Flask(__name__)
@app.route('/', methods=['GET'])
def welcome():
    #res= "Hello world!Welcome to calculator"
    return render_template("index.html")

@app.route('/calc', methods=['GET','POST'])
def calculate():
    if request.method == 'POST':
        print("in post request")
        num1 = int(request.get_json().get('value1'))
        print(num1)
        num2= int(request.get_json().get('value2'))
        print(num2)
        op= request.get_json().get('operation')
        print(op)
    else:
        print("in get request")
        num1 = request.args.get('value1',type = int)
        print(num1)
        num2= request.args.get('value2',type = int)
        print(num2)
        op= request.args.get('operation',type = str)
        print(op)

    if (op == '+'):
        res= str(num1+num2)
    elif(op == '-'):
        res= str(num1-num2)
    elif(op == '*'):
        res= str(num1*num2)
    elif(op == ' '):
        op='+'
        res= str(num1+num2)
    else:
        res= "Invalid operation"
    return render_template('index.html', val1=num1, val2 =num2, operation = op, sol = res)
    
if __name__ == '__main__':
    app.run(debug=True)