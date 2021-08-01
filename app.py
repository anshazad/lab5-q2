import json
from flask import Flask, render_template, request, jsonify   

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("InputOutput.html")    
    

@app.route("/submitJSON", methods=["POST"])
def processJSON():

    jsonStr = request.get_json()
    #print(jsonStr)
    jsonObj = json.loads(jsonStr)
    response = ""
    s=jsonObj['l']
    l=s.split(",")
    def duplicate_remover(lst):
        length=len(lst)
        for i in range(length):
            if lst[i] not in lst[0:i]:
                lst.append(lst[i])
            else:
                continue
        l[:length]=[]
        l.reverse()
    duplicate_remover(l)
    for i in range(len(l)):
        response+="{},".format(l[i])
    
    return response    
  
    
    	    
    
    
    
if __name__ == "__main__":
    app.run(debug=True)
    
    
