from flask import request, redirect, render_template, session, flash, Flask

app = Flask(__name__)
app.config['DEBUG'] = True 

