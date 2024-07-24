from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route('/', methods=['GET'])
def ping():
    return 'this works!'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
