# import dependencies
import os
from flask import Flask, render_template

# bootstrap the app
app = Flask(__name__)

# set the port dynamically with a default of 3000 for local development
port = int(os.getenv('PORT', '3000'))

# our base route which just returns a string
@app.route('/')
def hello_world():
    return 'Congrats, you made your first website!!!'

@app.route('/index')
def with_string():
    html = """
        <h1> This is a paragraph </h1>
        <li>list</li>
        """
    return html

@app.route('/withtemplate')
def other_view():
    return render_template("test.html")

@app.route('/better')
def with_css():
    my_name = "Marcelo"
    return render_template("withcss.html", name=my_name)

# start the app
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port, debug=True)