from flask import Flask, render_template, request
import pickle
import numpy as np
import pandas as pd
import traceback

app = Flask(__name__)
app.debug = True


with open('svm_classifier.pkl', 'rb') as model_file:
    model = pickle.load(model_file)
with open('scaler.pkl', 'rb') as scaler_file:
    scaler = pickle.load(scaler_file)

@app.route('/', methods=['GET', 'POST'])
def home():
    prediction_text = ''
    if request.method == 'POST':
        try:

            math_score = request.form['math_score']
            reading_score = request.form['reading_score']
            writing_score = request.form['writing_score']

            feature_names = ['math_score', 'reading_score', 'writing_score']
            features = pd.DataFrame([[float(math_score), float(reading_score), float(writing_score)]],
                                    columns=feature_names)

            features_scaled = scaler.transform(features)

            prediction = model.predict(features_scaled)

            prediction_text = f'Predicted Race/Ethnicity Group: {prediction[0]}'

        except Exception as e:
            traceback.print_exc()
            prediction_text = f'Error: {e}'

    # Render the index.html with the prediction text
    return render_template('index.html', prediction_text=prediction_text)

if __name__ == '__main__':
    app.run(port=5000, debug=True)