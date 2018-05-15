from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Miguelle'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The avengers movie was so cool'
        },
        {
            'author': {'username': 'Tamara'},
            'body': 'I would like to move to a new city!'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)