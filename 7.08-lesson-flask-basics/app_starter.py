# anqconda prompt
# python app_starter.py

# imports
from flask import Flask, request, jsonify, Response, render_template
import pandas as pd
import numpy as np

# initialize the flask app

app=Flask('myapi')

# route 1: hello 

@ app.route('/')
def home():
# return a simple string
    return 'Hello World'
# route 2: return a 'web page'
# return some hard-coded html

@app.route('/hc')
def hc_page():
        # return some hard-coded html
        return '<html><body><h1>This is a hard coded page!</h1><p>Here is some hard-coded content. Isn\'t it pretty?</p></body></html'

# route 3: return some data

@app.route('/hc_json')
def hc_json():
# create some data to return as json
    js = {'user_id':'pwd', 'first_name' = 'Darth', 'last_name':'Vader'}
# use flask's jsonify function to return the data as well as a 200 status code

    return jsonify(js), 200  


# route 4: show a form to the user
# use flask's render_template function to display an html page


# route 5: accept the form submission and do something fancy with it
# load in the form data from the incoming request
# manipulate data into a format that we pass to our model


# Call app.run(debug=True) when python script is called

if __name__= '__main__'
    app.run(debug=True)