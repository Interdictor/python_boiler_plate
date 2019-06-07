from flask import Flask
from flask import render_template
app = Flask(
    __name__,
    static_folder='delivery/static',
    template_folder='delivery/templates',
)

@app.route('/')
def hello_world():
    return render_template('hello.html')

app.config['PROPAGATE_EXCEPTIONS'] = False
app.config['TEMPLATES_AUTO_RELOAD'] = True
