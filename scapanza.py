'''
Created on 
Course work: 
@author: Ishita
Source:
    
'''
# with path variable return a dict consists of 
# state and population of city supplied through parameter


# # Import necessary modules

from flask import Flask, render_template, jsonify
import random, json

app = Flask(__name__)

@app.route('/')
def start():

    index = random.randrange(0,2)
    city = [{
        "city"   : "Chennai",
        "state"  : "Tamilnadu",
        "population": "7.8 million"    
    },
    {
        "city"   : "Toronto",
        "state"  : "Ontario",
        "population" : "6.8 million"
    }
]


    # return render_template('index.html')
    return jsonify(city[index])

@app.route('/city/<city>')
def city_pop(city):

    f = open("info.json")
    json_data = json.load(f)
    for cities in json_data['city_info'] :
        
        if cities["city"] == city :
            return jsonify([cities])



if __name__== "__main__":
    app.run(host="0.0.0.0", debug = True, port = 4581)