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

@app.route("/", methods = ["GET","POST"])
def index():
    if request.method == "POST":
        pass
    else:
        return render_template("index.html")

ifd __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)