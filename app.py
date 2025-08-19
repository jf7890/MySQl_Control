from flask import Flask, render_template, request, redirect, url_for
import control
from routes import routes
app = Flask(__name__, template_folder='templates', static_folder='static')

app.register_blueprint(routes, url_prefix='/')

if __name__ == "__main__":
    app.run(debug=True)
    