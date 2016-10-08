import pickle
import io

f = io.open('data', 'rb')
data = pickle.load(f)
f.close()

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/data/<month>')
def get_month_data(month):
    print month
    if not month in data:
        return "not available"
    return data[month]

if __name__ == "__main__":
    print data.keys()
    app.run()
