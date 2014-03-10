import datetime

from flask import render_template

from app import app, pages


@app.route('/')
def home():
    return render_template('index.html', now=datetime.datetime.now())


@app.route('/<path:path>/')
def page_detail(path):
    # Path is the filename of a page, without the file extension
    # e.g. "first-post"
    page = pages.get_or_404(path)

    all_pages = sorted(
        [p for p in pages if 'date' in p.meta],
        reverse=True,
        key=lambda p: p.meta['date']
    )

    if len(all_pages) > 10:
        all_pages = all_pages[0:10]

    return render_template('page.html', page=page, pages=all_pages, now=datetime.datetime.now())


@app.route('/projects/')
def projects():
    return render_template('projects.html', now=datetime.datetime.now())


@app.route('/blog/')
def blog():
    all_pages = sorted(
        [p for p in pages if 'date' in p.meta],
        reverse=True,
        key=lambda p: p.meta['date']
    )

    return render_template('archive.html', pages=all_pages, now=datetime.datetime.now())
