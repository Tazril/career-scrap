from flask import Flask, render_template, request

from driver import MainDriver

driver = MainDriver()
app = Flask(__name__)
LIMIT = 100


def get_jobs(request):
    text = ''
    if request.method == 'POST':
        text = request.form['search']
    if request.args.get('search'):
        text = request.args.get('search')
    if text:
        jobs = driver.repository.search_postings(text)
    else:
        jobs = driver.repository.get_postings()
    return text, jobs


def get_paginated_jobs(jobs):
    page = 0
    if request.args.get('page'):
        page = int(request.args.get('page'))
    total = (len(jobs) + LIMIT - 1) // LIMIT
    paginated = jobs[page * LIMIT: (page + 1) * LIMIT]
    return paginated, page, total


@app.route("/", methods=['GET', 'POST'])
def home():
    text, jobs = get_jobs(request)
    paginated, page, total = get_paginated_jobs(jobs)
    return render_template('index.html', jobs=paginated, search=text, total=total, page=page)


if __name__ == '__main__':
    driver.start()
    app.run()
