from flask import Flask, render_template, request
import joblib
import numpy as np

app = Flask(__name__)

# Load the trained model and scaler
model = joblib.load('model.pkl') 
scaler = joblib.load('scaler.pkl')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Get input values from the form
    age = int(request.form['age'])
    sex = int(request.form['sex'])
    bmi = float(request.form['bmi'])
    children = int(request.form['children'])
    smoker = int(request.form['smoker'])
    region = int(request.form['region'])

    # Create a NumPy array and scale it
    input_data = np.array([[age, sex, bmi, children, smoker, region]])
    scaled_input = scaler.transform(input_data)

    # Make prediction
    prediction = model.predict(scaled_input)[0]

    return render_template('index.html', prediction_text=f'Estimated Insurance Cost: ${prediction:.2f}')

if __name__ == '__main__':
    app.run(debug=True)


