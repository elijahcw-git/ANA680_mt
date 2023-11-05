from flask import Flask, render_template, request
import pickle

app = Flask(__name__)
app.debug = True
# Load the SVM model and scaler from disk
with open('svm_classifier.pkl', 'rb') as model_file:
    model = pickle.load(model_file)
with open('scaler.pkl', 'rb') as scaler_file:
    scaler = pickle.load(scaler_file)


@app.route('/', methods=['GET', 'POST'])
def home():
    prediction_text = ''
    if request.method == 'POST':
        try:
            features = [float(x) for x in request.form.values()]
            scaled_features = scaler.transform([features])
            prediction = model.predict(scaled_features)
            race_ethnicity_groups = ['Group A', 'Group B', 'Group C', 'Group D', 'Group E']
            prediction_text = f'The predicted race/ethnicity group is: {race_ethnicity_groups[int(prediction[0])]}'
        except Exception as e:
            prediction_text = f"Error in prediction: {e}"

    return render_template('index.html', prediction_text=prediction_text)



if __name__ == '__main__':
    app.run(debug=True)

