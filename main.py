import datetime

from flask import Flask, render_template, request

from driver import MainDriver

driver = MainDriver()
app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        text = request.form['search']
        return render_template('index.html', jobs=driver.repository.search_postings(text), search=text)
    return render_template('index.html', jobs=driver.repository.get_postings())


@app.route("/refresh")
def refresh():
    driver.update_data()
    return "Data Refreshed " + str(datetime.datetime.now())


if __name__ == '__main__':
    app.run()
