**Use Case : Diabetes Prediction**

**Problem Statement:**
A healthcare provider wants to predict whether a patient is diabetic based on a dataset containing health indicators such as glucose level, BMI, age, and blood pressure.

**Assessment Tasks:**

**Data Preprocessing:**

Handle missing or incorrect data entries.

Scale numerical features using standardization or normalization.

Split the data into training, validation, and test sets.

**Model Training and Evaluation:**

Train any one classification model (e.g., Logistic Regression, Decision Tree Classifier, NaiveBayes ).

Evaluate models using accuracy_Score, and classification reports.

**Model Deployment:**
Build a Flask application where healthcare professionals can input patient data and receive a prediction.

Add a feature to display the probability score of being diabetic.

**Common Deployment Requirements:**

**Flask Web Application:**

Implement input forms to gather user data.

Use Flask's @app.route and POST/GET methods for form submission and model prediction.

**Model Integration:**

Save the trained model using joblib or pickle.

Load the saved model in the Flask application.

**UI/UX Enhancements:**

Use HTML and CSS to make the interface user-friendly.

Add validation for form fields to ensure correct data input.

**Deployment:**
Deploy Flask Web app in local server.

test the model 

**Dataset Overview: Diabetes Database**
Source: National Institute of Diabetes and Digestive and Kidney Diseases  - 

Link: **Refer CSV file. attached this repo**

**Description:**
The dataset includes diagnostic data to predict whether a patient has diabetes based on certain diagnostic measurements.

Binary classification problem: Outcome (1 = Diabetic, 0 = Non-Diabetic).

**Features:**

**Pregnancies**: Number of times pregnant

**Glucose**: Plasma glucose concentration

**BloodPressure**: Diastolic blood pressure (mm Hg)

**SkinThickness**: Triceps skinfold thickness (mm)

**Insulin**: 2-Hour serum insulin (mu U/ml)

**BMI**: Body mass index (weight in kg/(height in m)^2)

**DiabetesPedigreeFunction**: Function to estimate genetic influence

**Age**: Age in years

**Outcome**: Target variable (1 = Diabetes, 0 = No Diabetes)


