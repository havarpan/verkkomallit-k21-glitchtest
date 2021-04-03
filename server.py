from flask import Flask, render_template, jsonify
from random_graph import json_graph

from lplib import ryhma1

app = Flask(__name__, static_folder='js_css', template_folder='html')

@app.route("/", methods = ['GET'])
def index():
    return render_template('index.html')
@app.route('/', methods = ['POST'])
def newgraph():
    return jsonify(json_graph())

  
@app.route("/ryhma1", methods = ['GET'])
def ryhma1_get():
    return render_template('ryhma1/index.html')
@app.route("/ryhma1", methods = ['POST'])
def ryhma1_post():
    return jsonify(ryhma1())
  
if __name__ == "__main__":
    app.run()