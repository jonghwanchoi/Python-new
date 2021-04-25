from flask import Flask, request, jsonify
from flask import render_template
from dataList import getData
from readDB import DBread

app = Flask(__name__)

@app.route('/')
def RestArea():
    list = getData()
    return render_template('list.html', list=list)

@app.route('/temp')
def temper():
    list = DBread()
    return render_template('test.html', list=list)

if __name__ == "__main__":
    app.run(host="localhost")