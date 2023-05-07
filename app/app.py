import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__, static_url_path='')
app.debug = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///manifestation.db'
db = SQLAlchemy(app)

if __name__ == '__main__':
    app.run(debug=True)