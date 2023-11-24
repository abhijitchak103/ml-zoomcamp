# import requests
import pickle

# url = 'http://localhost:9696/predict'

customer = {"job": "retired", 
            "duration": 445, 
            "poutcome": "success"}

# Load DictVectoizer
with open('dv.bin', 'rb') as f_in:
    dv = pickle.load(f_in)

# Load Logistic Regressor model
with open('model1.bin', 'rb') as f_in:
    model = pickle.load(f_in)


# Better to put this 3 lines of core logic in a different function
X = dv.transform([customer])
y_pred = model.predict_proba(X)[0, 1]
credit = y_pred >= 0.5

result = {
    'credit_probability': float(round(y_pred, 3)),
    'credit': bool(credit)
}

# print(requests.post(url, json=customer).json())

# response = requests.post(url, json=customer).json()
# if response['churn']:
#     print("Sending promo email to Customer")
# else:
#     print("Not sending promo email to Customer")

print(result['credit_probability'])