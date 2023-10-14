
import requests

url = 'http://localhost:9696/predict'

customer = {
   "gender": "female",
   "seniorcitizen": 0,
   "partner": "yes",
   "dependents": "no",
   "phoneservice": "no",
   "multiplelines": "no_phone_service",
   "internetservice": "dsl",
   "onlinesecurity": "no",
   "onlinebackup": "yes",
   "deviceprotection": "no",
   "techsupport": "no",
   "streamingtv": "no",
   "streamingmovies": "no",
   "contract": "month-to-month",
   "paperlessbilling": "yes",
   "paymentmethod": "electronic_check",
   "tenure": 2,
   "monthlycharges": 29.85,
   "totalcharges": 29.85*2
}


print(requests.post(url, json=customer).json())

response = requests.post(url, json=customer).json()
if response['churn']:
    print("Sending promo email to Customer")
else:
    print("Not sending promo email to Customer")



