from flask import Blueprint, render_template, request

client_blueprint = Blueprint('client_blueprint', __name__)


@client_blueprint.route('/dashboard')
@client_blueprint.route('/notifications')
@client_blueprint.route('/file-explorer')
@client_blueprint.route('/')
def index():
    return render_template("index.html")
