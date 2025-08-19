from flask import Blueprint, Flask, render_template, request, redirect, url_for
import control
routes = Blueprint('routes', __name__)

@routes.route('/')
def index():
    return render_template('index.html')

@routes.route('/logs')
def watch_logs():
    logs = control.parse_mysql_log()
    return render_template('Raw_logs.html', logs=logs)

@routes.route('/danger_logs')
def danger_logs():
    danger_logs = control.is_danger(control.parse_mysql_log())
    return render_template("Danger_logs.html", logs=danger_logs)
