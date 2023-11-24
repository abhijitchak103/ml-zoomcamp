import requests

url = "http://localhost:8080/2015-03-31/functions/function/invocations"

# AWS API url
# url = "https://9op3cdr9g5.execute-api.ap-south-1.amazonaws.com/test/predict"

data = {'url': 'http://bit.ly/mlbookcamp-pants'}

result = requests.post(url, json=data).json()
print(result)