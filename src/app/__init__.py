from flask import Flask
from config import BASE_DIR
from flask import render_template

app = Flask(__name__)
from app import views
app.config.from_object('config')
