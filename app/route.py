from flask import render_template


def index():
    return render_template('index.html', message='$9925999.8787',message2='**00**')
