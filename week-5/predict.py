
# Imports
import pickle
from flask import Flask, request, jsonify


# Parameters
input_file = 'model_C=1.0.bin'


# Load the Model
with open(input_file, 'rb') as f_in:
    dv, model = pickle.load(f_in) 

# Initialize the app
app = Flask('ping')

# Define the predict function
@app.route('/predict', methods=['POST'])
def predict():
    customer = request.get_json()


    # Better to put this 3 lines of core logic in a different function
    X = dv.transform([customer])
    y_pred = model.predict_proba(X)[0, 1]
    churn = y_pred >= 0.5
    
    result = {
        'churn_probability': float(round(y_pred, 3)),
        'churn': bool(churn)
    }
    
    return jsonify(result)


if __name__ == '__main__':
    app.run(debug=True,
            host='0.0.0.0',
            port=9696)
