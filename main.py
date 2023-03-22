# Importing flask module in the project is mandatory
# An object of Flask class is our WSGI application.
from flask import Flask, request

# current module (__name__) as argument.
app = Flask(__name__)

# The route() function of the Flask class is a decorator,
# which tells the application which URL should call
# the associated function.
@app.route('/')
def return_client_IP():
    return 'Hello your IPv4 is: {}'.format(request.remote_addr)

# main driver function
if __name__ == '__main__':

 # run() method of Flask class runs the application
 # on the local development server.
 app.run(host='0.0.0.0', port=3003)
