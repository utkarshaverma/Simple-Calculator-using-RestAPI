# Simple-Calculator-using-RestAPI
A simple Rest API demonstration using Flask. Resolves GET and POST request for operations of addition, subtraction and multiplication.

$ python3 install pip3
$ pip3 install virtualenv
$ virtualenv myenv
$ source myenv/bin/activate
(env)$ pip3 install flask

Postman:

GET request:
localhost:5000/clac?value1=3&value2=4&operation=*
answer: 12

POST request:
localhost:5000/clac
{"value1":"3","value2":"4","operation":"+"}
answer: 7
