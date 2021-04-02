from flask import Flask, render_template, jsonify
from random_graph import get_json

app = Flask(__name__, static_folder='public', template_folder='views')

@app.route('/', methods = ['POST'])
def newgraph():
    return jsonify(get_json())
  
@app.route("/", methods = ['GET'])
def index():
    return render_template('index.html')
  
if __name__ == "__main__":
    app.run() 