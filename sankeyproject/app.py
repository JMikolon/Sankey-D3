from flask import Flask, render_template,json, current_app as app
from flask import jsonify
import os
import json
from flask import request




app = Flask(__name__)

@app.route("/")


def home():    
    return render_template("index.html")

@app.route('/data')
def data():
   
    file_path = "static/data/hochtief.json"
    with open(file_path, "r") as file_data:
        json_data = json.load(file_data)

    print(request.query_string)
    return jsonify(json_data) 
"""
    args = request.args

    print(args)

    
    if args['date'] == '10.09.1986':
        print('jo')
    else:
        print('no')
    
"""
  


if __name__ == "__main__":
    app.run(debug=True)