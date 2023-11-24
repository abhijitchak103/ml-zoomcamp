
# Imports
import pickle
from flask import Flask, request, jsonify


# Load DictVectorizer
with open('dv.bin', 'rb') as f_in:
    dv = pickle.load(f_in) 

# Load Log Regression Model
with open('model2.bin', 'rb') as f_in:
    model = pickle.load(f_in) 

# Initialize the app
app = Flask('ping')

# Define the predict function
@app.route('/predict', methods=['POST'])
def predict():
    customer = request.get_json()


    # Better to put this 3 lines of core logic in a different function
    X = dv.transform([customer])
    y_pred = model.predict_proba(X)[0, 1]
    credit = y_pred >= 0.5
    
    result = {
        'credit_probability': float(round(y_pred, 3)),
        'credit': bool(credit)
    }
    
    return jsonify(result)


if __name__ == '__main__':
    app.run(debug=True,
            host='0.0.0.0',
            port=8080)
