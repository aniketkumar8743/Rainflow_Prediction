# Rainflow - Rainfall Prediction using Machine Learning

## Overview
Rainflow is a machine learning project that predicts rainfall using weather data. The model is built using a **Random Forest Classifier** and achieves an **accuracy of approximately 76.6%**, as shown in the evaluation metrics. The project leverages **MLflow** for experiment tracking and **Flask** for deploying an API to make predictions.

<img width="392" alt="image" src="https://github.com/user-attachments/assets/1a7712c1-0a22-473f-ac26-eacd8281ccde" />

## Features
- Uses **Random Forest Classifier** for rainfall prediction.
- Tracks model performance and versioning using **MLflow**.
- Provides a **Flask API** for real-time predictions.
- Dockerized setup for easy deployment.

## Project Structure
```
RAINFLOW/
│── templates/
│   ├── index.html
│── app.py
│── dockerfile
│── Rainfall Prediction.ipynb
│── Rainfall.csv
│── requirements.txt
```

## Model Performance
### Classification Report
```
'0': {'precision': 0.8421, 'recall': 0.6667, 'f1-score': 0.7442, 'support': 24},
'1': {'precision': 0.7143, 'recall': 0.8696, 'f1-score': 0.7843, 'support': 23},
Accuracy: 0.7659
Macro Avg: {'precision': 0.7782, 'recall': 0.7681, 'f1-score': 0.7642, 'support': 47}
Weighted Avg: {'precision': 0.7796, 'recall': 0.7659, 'f1-score': 0.7638, 'support': 47}
```

## MLflow Integration
- MLflow is used to track model versions, performance metrics, and hyperparameters.
- The best-performing model is stored and loaded dynamically in the Flask API.

## Flask API
The Flask app allows users to send weather data and get rainfall predictions.

### Endpoints:
- **Home** (`/`) - Renders the HTML form.
- **Predict** (`/predict`) - Accepts input parameters and returns the predicted result.

### How to Run
```sh
# Install dependencies
pip install -r requirements.txt

# Run Flask app
python app.py
```
By default, the Flask app runs on port **5001** since MLflow uses **5000**.

## Docker Setup
To run the project in a Docker container:
```sh
docker build -t rainflow .
docker run -p 5001:5001 rainflow
```

## Dependencies
Ensure you have the following packages installed:
```
Flask
mlflow
pandas
scikit-learn
matplotlib
```

## Future Improvements
- Hyperparameter tuning to improve accuracy.
- Integration with a database to store predictions.
- Deployment on cloud services.

## Author
Developed by **[Your Name]**


