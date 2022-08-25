# create flask api for the app
from flask import Flask, jsonify, request, abort
import httpx
app = Flask(__name__)

# create / post endpoint for the app
@app.route('/', methods=['POST'])
def create_task():
    # get body data from the request
    body = request.get_json()
    # check if the body is empty
    if not body:
        abort(400)
    # return the body data
    operate(data)
    return jsonify(body)


# parse mime data into dictionary
def parse_mime(data):
    # parse the data into a dictionary
    data = dict(data)
    return data

def operate(data):
    # do something with the data

    # create a thread to do the work

    value_a = func1(1)
    value_b = func2(1)
    value_c = func3(1)
    formula = 0.2 * int(value_a) + 0.3 * int(value_b) + 0.5 * (value_c)
    return formula
    # return thread1 , thread2 , thread3

def func1(data):
    # do something
    return 1

def func2(data):
    # do something
    return 1

def func3(data):
    # do something
    return 1

if __name__ == '__main__':
    # thread1 = threading.Thread(target=func1, args=(1))
    # thread2 = threading.Thread(target=func2, args=(1))
    # thread3 = threading.Thread(target=func3, args=(1))
    app.run(debug=True)