from flask import Flask, render_template, jsonify
from random_graph import json_graph

# ryhmät listataan tähän
# myös tämän tiedoston loppuun
# ynnä itse lplib-tiedostoon
from lplib import ryhma1, ryhma2


# webserver (= flask) -konfiguraatio ja juurihakemisto
app = Flask(__name__, static_folder='js_css', template_folder='html')

@app.route("/", methods = ['GET'])
def index():
    return render_template('index.html')
@app.route('/', methods = ['POST'])
def newgraph():
    return jsonify(json_graph())


# kullekin ryhmälle omat endpointit
@app.route("/ryhma1", methods = ['GET'])
def ryhma1_get():
    return render_template('ryhma1/index.html')
@app.route("/ryhma1", methods = ['POST'])
def ryhma1_post():
    return jsonify(ryhma1())

@app.route("/ryhma2", methods = ['GET'])
def ryhma2_get():
    return render_template('ryhma2/index.html')
@app.route("/ryhma2", methods = ['POST'])
def ryhma2_post():
    return jsonify(ryhma2())

  
# tämä käynnistää webserverin
if __name__ == "__main__":
    app.run()