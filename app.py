

from flask import Flask,render_template_string,render_template, request
import json

from flask_cors import CORS, cross_origin
from parking.pakring_api import parking_api;

import json
app = Flask(__name__)
CORS(app)


@app.route('/')
def index():
    return render_template('index.html')

    return render_template("Risk_input.html")


      
@app.route('/react_to_flask', methods=['POST','PUT'])
def react_to_flask():
    print(request)
    if request.method == 'POST':
        print(request.get_json)
    #parsed_request = re   quest.files.get('file') 
    #fileName = np.asarray(request.form.get('fileName'), dtype = int)
        print("dfdfdfdfd",request.form)
    
        parsed_request = request.form.get('data').split(",")

        print(parsed_request)
   
   
   
    if request.method=='PUT':
        parsed_request = request.form.get('data').split(",")
    
    #parsed_request
    """
    dir_path = os.path.dirname(os.path.realpath(__file__))
    dir_path = dir_path + "\data"
    saved_file_path = os.path.join(dir_path, fileName)
    parsed_request.save(saved_file_path) 	# saved_file_path 경로에 받은 file 저장"""

    return "parsed_request"

@app.route('/parking_data', methods=['POST','PUT'])
def parking_data():
    print("dfdfdfdfd",request.form)
    if request.method == 'POST':
        print(request.get_json)
        parking_api(request.data)
        print("dfdfdfdfd",request.data)
        return [100,200,300,400,500]
    
   
    if request.method=='PUT':
        print(request.data)
        #parsed_request = json.load(request.data)
        print("dfdfdfdfd",request)
        return [600,700,800,900,1000]


    
@app.route('/hello')
def hello():
    return ""


if __name__ == '__main__':
   
    app.run(host="0.0.0.0", port="4500",  debug=True)