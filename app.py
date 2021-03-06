# -*- coding: utf-8 -*-
from flask import Flask, render_template, request, json
from requests import get
from bs4 import BeautifulSoup


app = Flask(__name__)
app.config.from_object('config')


def get_currency():
    try:
        result = get('https://www.cbr-xml-daily.ru/daily_utf8.xml')
        html = result.content
        soup = BeautifulSoup(html, 'lxml')
        text = soup.find("valute", id="R01235")
        rate = float(text.find("value").get_text().replace(',', '.'))
        return rate
    except ConnectionError:
        print("CBR server did not response. Please, try again later")
    except (AttributeError, TypeError):
        print("Could not receive data from CBR")


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/convert', methods=['POST'])
def convert():
    rate = get_currency()
    usd = request.form['inputUSD']
    result = float(usd) * rate
    return json.dumps({'result': '{0:.2f}'.format(result)})


if __name__ == '__main__':
    app.run(debug=True)
