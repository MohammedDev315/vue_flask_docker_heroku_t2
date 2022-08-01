from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/' , methods=['GET'])
def home():
    return 'welcome from vue flask app test 22 github'

if __name__ == '__main__':
    app.run()
