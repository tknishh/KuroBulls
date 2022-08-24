import requests

URI = "http://localhost:5000/"
def BertModelOutput(text):
    response = requests.post(URI, json={'data': "I am a spammer."})
    return response.json()