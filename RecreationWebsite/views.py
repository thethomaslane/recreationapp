"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template
from RecreationWebsite import app
from RecreationWebsite.forms import ActivityForm

@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    return render_template(
        'index.html',
        title='Home Page',
        year=datetime.now().year,
    )

@app.route('/contact')
def contact():
    """Renders the contact page."""
    return render_template(
        'contact.html',
        title='Contact',
        year=datetime.now().year,
        message='Your contact page.'
    )

@app.route('/about')
def about():
    """Renders the about page."""
    return render_template(
        'about.html',
        title='About',
        year=datetime.now().year,
        message='Your application description page.'
    )

@app.route('/form',  methods=['GET', 'POST'])
def form():
    results=""
    form = ActivityForm()
    if form.validate_on_submit():
        outdoors = form.outdoors.data
        activity = form.active.data
        if outdoors and activity:
            results="Go for a hike"
        if outdoors and not activity:
            results="Go lay out on the beach"
        if (not outdoors) and activity:
            results = "Go to the gym"
        if (not outdoors) and (not activity):
            results = "Go shopping at the mall"
    return render_template('activity.html', title='Activity', form=form,results=results)
