from flask import Flask, request, render_template_string
from configuration import Conf
from flask import render_template
from scripts.script import flag

app = Flask(__name__, static_folder="static" , static_url_path='')

# Configure app. Can use config.items() to see all properties;
app.config.from_object(Conf)
app.secret_key = flag


# Home page route;
@app.route("/")
def index_page():
    name = request.args.get('name') or None
# Basic template with <name> variable in it
    template = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>
    </title>
    <link rel="stylesheet" type="text/css" href="{{ url_for('static', filename='stylesheets/main_css.css') }}" >

</head>
<body>
        <!-- All images and .css from static/stylesheets -->

        <div class = "container">
            <a href="#">
            <div class = "card">
                    <div class = "imgBox">
                        <img src="{{ url_for('static', filename ='stylesheets/coding.png') }}"  alt="Coding">
                        <h3>Design</h3>
                    </div>

                    <div class = "content">
                        <p>From fairest creatures we desire increase,
                            That thereby beauty's rose might never die,
                            But as the riper should by time decease,
                            His tender heir might bear his memory</p>
                        <p hidden> %s </p>
                    </div>
            </div>
            </a>

             <a href="/code">
            <div class = "card">
                    <div class = "imgBox">
                        <img src=" {{ url_for("static", filename = "stylesheets/planning.png")}}"  alt="Planning">
                        <h3>Code</h3>
                    </div>
                    <div class = "content">
                        <p>From fairest creatures we desire increase,
                            That thereby beauty's rose might never die,
                            But as the riper should by time decease,
                            His tender heir might bear his memory</p>
                    </div>
            </div>
            </a>

            <a href="#">
                    <div class = "card">
                            <div class = "imgBox">
                                 <img src=" {{ url_for("static", filename = "stylesheets/statringup.png")}}"  alt="Startup">
                                <h3>Launch</h3>
                            </div>

                            <div class = "content">
                                <p>From fairest creatures we desire increase,
                                    That thereby beauty's rose might never die,
                                    But as the riper should by time decease,
                                    His tender heir might bear his memory</p>
                            </div>
                        </div>
                </a>
            </div>
</body>
</html>''' % name
    return render_template_string(template)


# Function, that finds all properties from user search on machine;
@app.route('/static/<path:path>/')
def handler(path):
    if "script.py" not in path:
        try:
            with open(f"static/{path}") as file:
                data = file.read()
                file.close()
            return data
        except Exception:
            return render_template("index.html")
    else:
        return render_template("index.html")


@app.route("/code")
def code_index():
    return render_template("source_page.html")


# Basic errorhandler
@app.errorhandler(404)
def page_not_found(e):
    return render_template("index.html"), 404
