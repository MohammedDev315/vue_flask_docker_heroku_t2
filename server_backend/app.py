from crypt import methods
from flask import Flask

app = Flask(__name__)

@app.route('/' , methods=['GET'])
def home():
    return 'welcome from vue flask app test 22'

if __name__ == '__main__':
    app.run(host='0.0.0.0')
