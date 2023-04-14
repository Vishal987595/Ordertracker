from flask import Flask, render_template, request, redirect, url_for, session
import flask

import MySQLdb.cursors

app = Flask(__name__)
from configure import config
mysql = config(app)

from outlet import outlet
from customer import customer
app.register_blueprint(outlet)
app.register_blueprint(customer)

if __name__ == '__main__':
    app.run(debug=True)