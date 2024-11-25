from flask import Flask, request, jsonify, render_template
import pickle
import numpy as np
import pandas as pd

# Load Model and Preprocessing Tools
with open('model.pkl', 'rb') as f:
    model = pickle.load(f)
with open('scaler.pkl', 'rb') as f:
    scaler = pickle.load(f)
with open('encoders.pkl', 'rb') as f:
    encoders = pickle.load(f)

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Extract Input Data
        input_data = request.form
        data = {
            'Age': float(input_data['Age']),
            'RestingBP': float(input_data['RestingBP']),
            'Cholesterol': float(input_data['Cholesterol']),
            'MaxHR': float(input_data['MaxHR']),
            'Oldpeak': float(input_data['Oldpeak']),
            'Sex': input_data['Sex'],
            'ChestPainType': input_data['ChestPainType'],
            'FastingBS': input_data['FastingBS'],
            'RestingECG': input_data['RestingECG'],
            'ExerciseAngina': input_data['ExerciseAngina'],
            'ST_Slope': input_data['ST_Slope']
        }
        print(data)
        # Encode Categorical Features
        print(encoders.keys())
        for col in encoders.keys():
            data[col] = encoders[col].transform([data[col]])[0]
        

        # Convert to DataFrame with Correct Feature Order
        feature_order = ['Age','Sex','ChestPainType', 'RestingBP', 'Cholesterol','FastingBS', 'RestingECG', 'MaxHR',  
                        'ExerciseAngina','Oldpeak','ST_Slope']
        df_input = pd.DataFrame([data], columns=feature_order)
        #print(df_input)

        # Scale Numerical Features
        numerical_features = ['Age', 'RestingBP', 'Cholesterol', 'MaxHR', 'Oldpeak']
        df_input[numerical_features] = scaler.transform(df_input[numerical_features])
        print(df_input)

        # Make Prediction
        prediction = model.predict(df_input)[0]
        print(prediction)
        result = 'Heart Disease' if prediction == 1 else 'No Heart Disease'

        # Render the result in the HTML page
        return render_template('index.html', prediction_text=result)
    
    except KeyError as e:
        # Handle missing form data
        return render_template('index.html', prediction_text=f"Error: Missing data for {str(e)}")

    except ValueError as e:
        # Handle invalid data types (e.g., non-numeric inputs)
        return render_template('index.html', prediction_text=f"Error: Invalid input data. Please enter valid numbers for all fields.")

    except Exception as e:
        # Catch any other exceptions and log the error message
        return render_template('index.html', prediction_text=f"An unexpected error occurred: {str(e)}")

if __name__ == '__main__':
    app.run(debug=True)
