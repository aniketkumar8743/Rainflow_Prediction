from flask import Flask, request, jsonify, render_template
import mlflow
import pandas as pd

# Initialize Flask App
app = Flask(__name__, template_folder="templates")

# Set MLflow tracking URI
mlflow.set_tracking_uri("http://127.0.0.1:5000")
model_name = "Random Forest Model Data"
current_model_uri = f"models:/{model_name}@ani"

# Load the model from MLflow
model = mlflow.sklearn.load_model(current_model_uri)

# Home Route
@app.route('/')
def home():
    return render_template('index.html')

# Prediction Route
@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get input data from form
        input_data = {
            "day": request.form.get("day", type=int),
            "pressure": request.form.get("pressure", type=float),
            "maxtemp": request.form.get("maxtemp", type=float),
            "humidity": request.form.get("humidity", type=float),
            "cloud": request.form.get("cloud", type=float),
            "sunshine": request.form.get("sunshine", type=float),
            "winddirection": request.form.get("winddirection", type=float),
            "windspeed": request.form.get("windspeed", type=float)
        }

        # Convert to DataFrame
        input_df = pd.DataFrame([input_data], columns=['day', 'pressure', 'maxtemp', 'humidity', 'cloud', 'sunshine', 'winddirection', 'windspeed'])

        # Make Prediction
        prediction = model.predict(input_df)[0]

        # Interpret Prediction
        prediction_text = "Rainfall" if prediction == 1 else "No Rainfall"
        print("Prediction Result:", prediction_text)  # ✅ Print in the console for debugging

        return render_template('index.html', prediction_text=f'Predicted Rainfall: {prediction_text}')
    
    except Exception as e:
        return jsonify({"error": str(e)})

# Run Flask App
if __name__ == '__main__':
    app.run(debug=True)
