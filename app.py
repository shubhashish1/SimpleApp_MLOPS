from flask import Flask, render_template, request, jsonify
import os
import yaml
import joblib
import pandas as pd
import numpy as np
import json

params_path = "params.yaml"
webapp_root = "webapp"

static_dir = os.path.join(webapp_root, "static")
templates_dir = os.path.join(webapp_root, "templates")

app = Flask(__name__, static_folder = static_dir, template_folder = templates_dir)

def read_params(config_path):
    with open(config_path) as yaml_file:
        config = yaml.safe_load(yaml_file)
    return config

def predict(data):
    # Now let's load the data 
    config = read_params(config_path=params_path)
    model_dir_path = config["webapp_model_dir"]
    model = joblib.load(model_dir_path)
    prediction = model.predict(data)
    print(prediction[0])
    return prediction[0]

def api_response(request):
    try:
        data = np.array([list(request.json.values())])
        response = predict(data)
        response = {"response": response}
        return response
    except Exception as e:
        print(e)
        error = {"error": "Something went wrong!! Try again"}
        return error

@app.route("/", methods = ["GET","POST"])
def index():
    if request.method == "POST":
        # Here we also want to invoke the 404 error template incase of any error
        try:
            if request.form:
                data = dict(request.form)
                keys = list(data.keys())
                new_val=[float(list(data.values())[i][0]) for i in range(0,len(list(data.values())))]
                vals = vals=[[new_val[i]] for i in range(0,len(new_val))]
                # pd.DataFrame(dict(zip(keys, vals)))
                # data =  [float(list(data)[i][0]) for i in range(0,len(list(data)))]
                response = predict(pd.DataFrame(dict(zip(keys, vals))))
                return render_template("index.html",response=response)
                # return dict(request.form)
            elif request.json:
                response = api_response(request)
                return jsonify(response)
        except Exception as e:
            print(e)
            error = {"error":"Something went wrong! Please try again"}
            return render_template("404.html", error=error)
    else:
        return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)