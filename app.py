

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

@app.route('/Risk_result',methods = ['POST', 'GET'])
def result():
   if request.method == 'POST':

      result = request.form
      result_values = []
      for key,value in result.items():
          result_values.append(value)
      chart = json.dumps(Risk_assessment(result_values),ensure_ascii=False)
      print(result_values)
     
      #return render_template("result.html",result = result, chart = chart)
      return chart
      
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
    
    
   
    if request.method=='PUT':
        print(request.data)
        #parsed_request = json.load(request.data)
        print("dfdfdfdfd",request)
    return request.data

@app.route('/senddata')
def senddata():
   
    return ""

@app.route('/user/') 
def user():
    return render_template('index.html')
    
@app.route('/hello')
def hello():
    return ""
"""
def open_browser():
  webbrowser.open_new('http://0.0.0.0:'+str(port)+'/') 

port=9000
"""
"""
if __name__ == '__main__':
    ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
    ssl_context.load_cert_chain(certfile='cert.pem', keyfile='key.pem')
    app.run(host="0.0.0.0", port="5000",  debug=True ,ssl_context=ssl_context)
    """
if __name__ == '__main__':
   
    app.run(host="0.0.0.0", port="5000",  debug=True)