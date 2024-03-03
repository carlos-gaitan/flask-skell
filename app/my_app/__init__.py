from flask import Flask, render_template, request

from my_app.tasks.controllers import taskRoute
from my_app.config import DevConfig


app = Flask(__name__)
app.register_blueprint(taskRoute)
app.config.from_object(DevConfig)

@app.route('/')
def hello_world() -> str:
    zone = request.args.get('zone', 'NoNe')
    return render_template('index.html',zone=zone,items=[1,2,3,4,5,6,7,8,9],task='Very important task')



