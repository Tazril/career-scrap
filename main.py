from flask import Flask, render_template, request

from driver import MainDriver

driver = MainDriver()


class FlaskApp(Flask):
    def run(self, host=None, port=None, debug=None, load_dotenv=True, **options):
        driver.start()
        super(FlaskApp, self).run(host=host, port=port, debug=debug, load_dotenv=load_dotenv, **options)


app = FlaskApp(__name__)


@app.route("/", methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        text = request.form['search']
        return render_template('index.html', jobs=driver.repository.search_postings(text), search=text)
    return render_template('index.html', jobs=driver.repository.get_postings())


if __name__ == '__main__':
    app.run()
