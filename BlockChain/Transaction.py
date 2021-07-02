import requests


StatusCode = requests.post(
    'http://0.0.0.0:9000/Transaction', json={'Transaction': 'anudeep->test 100'})
print(StatusCode)
