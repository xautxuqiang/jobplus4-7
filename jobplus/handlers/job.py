from flask import Blueprint, render_template

job = Blueprint('job', __name__, url_prefix='/job')

@job.route('/')
def index():
    return render_template('job/index.html')
