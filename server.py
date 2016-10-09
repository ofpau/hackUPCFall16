import pickle
import io
import json
import urllib

import sys
reload(sys)
sys.setdefaultencoding("utf-8")

from flask import Flask, render_template
app = Flask(__name__)

data = {}

@app.route('/')
def hello_world():
    return render_template('index_test.html')

@app.route('/data/<month>')
def get_month_data(month):
    print "requesting month %s" % (month)
    if not month in data:
        f = io.open('data/' + month, 'rb')
        data[month] = pickle.load(f)
        f.close()
    print data[month][0]
    # carriers = list(set([x["fullCarrier"] for x in data[month]]))
    carriers = ["vodafone", "movistar", "orange", "yoigo"]
    readings = [x for x in data[month] if x["fullCarrier"] in carriers]
    #readings = data[month]
    return render_template('map_test.html', readings=readings[:500], carriers=carriers, month=month)

@app.route('/info')
def epic():
  return render_template('info.html')

if __name__ == "__main__":
    app.run()
