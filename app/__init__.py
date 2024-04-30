from flask import Flask
from .models import db

app = Flask(__name__)


# Add configurations here if needed
app.config.from_object('config')

db.init_app(app)

# Import views to register the routes
from . import views