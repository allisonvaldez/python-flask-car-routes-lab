#!/usr/bin/ env python3

# Import necessary utlities
import os
from flask import Flask, request, current_app, g, make_response

app = Flask(__name__)

existing_models = ['Beedle', 'Crossroads', 'M2', 'Panique']


"""
Provide the before_request decorator and absolute path.
"""
@app.before_request
def app_path():
    g.path = os.path.abspath(os.getcwd())

"""
ROUTE 1: Create the homepage index route for the app and provide the appropriate decorator. Set up the host, appname, and response body. It should display the proper message on page load.
"""
@app.route('/')
def index():

    # Create a simple HTML page to display the required message to the user
    response_body = "Welcome to Flatiron Cars"

    # Set the status code of OK and return the data
    status_code = 200

    # No headers needed at this route
    headers = {}

    return make_response(response_body, status_code, headers)

"""
ROUTE 2: Create the /<model> route for the app and provide the appropriate decorator. It should takes model variable and utilize the existing_models array. Perform error handling if the model does and doesn't exist.
"""
@app.route('/<model>')
def take_model(model):
    # Control flow for the application
    if model in existing_models:
        response_body = f"Flatiron {model} is in our fleet!"
        status_code = 200
    else:
        response_body = f"No models called {model} exists in our catalog"
        status_code = 404

    return make_response(response_body, status_code)

if __name__ == '__main__':
    app.run(port=5555, debug=True)