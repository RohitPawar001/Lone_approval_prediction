from flask import Flask, render_template, request
import os
import numpy as np
from sklearn.preprocessing import StandardScaler
from lone_approval_prediction.pipeline.prediction_pipeline import PredictionPipeline

app = Flask(__name__)

@app.route("/", methods=["GET"])
def homepage():
    return render_template("index.html")

@app.route("/train", methods=["GET"])
def training():
    os.system("python main.py")
    return "Training completed"

@app.route("/prediction", methods=["GET", "POST"])
def index():
    if request.method == "GET":
        return render_template("index.html")
        
    if request.method == "POST":
        try:
            
            cibil_score = float(request.form["Cibil Score"])
            loan_term = float(request.form["Loan Term"])
            education_encoded = float(request.form["Education"])
            no_of_dependents = float(request.form["Family Members"])
            self_employed_encoded = float(request.form["Employment"])

            
            features = np.array([[
                cibil_score,
                loan_term,
                education_encoded,
                no_of_dependents,
                self_employed_encoded
            ]])

            
            scaler = StandardScaler()
            scaled_features = scaler.fit_transform(features)

            
            obj = PredictionPipeline()
            predict = obj.predict(scaled_features)

            
            result = "Approved" if predict[0] == 1 else "Not Approved"
            
            return render_template("results.html", predictions=result)
            
        except Exception as e:
            print(f"Error during prediction: {str(e)}")
            return render_template("index.html", error="An error occurred during prediction. Please try again.")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)