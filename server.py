from flask import Flask, request
import json

app = Flask(__name__)

# GET request endpoint
@app.route('/regions/<region>', methods=['GET'])
def get_data(region):
    try:
        file=open("{}.json".format(region))
        data=json.load(file)
    except:
        data = "Error: region file doen't exist"
    return data

if __name__ == '__main__':
    app.run(debug=True, port=5000)