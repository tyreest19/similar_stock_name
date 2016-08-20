from find_trending_stocks import find_trending_stocks
from flask import Flask
from flask import render_template
from stocks import  get_stock_information
import os
import shutil

app = Flask(__name__)


@app.route("/",methods=['GET'])
def home_page():
    trending_stocks = find_trending_stocks()
    return render_template('homepage.html',trending_stocks=trending_stocks)

if __name__ == '__main__':
    app.run(debug=True)





















