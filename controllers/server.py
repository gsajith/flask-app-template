from flask import *

server = Blueprint('server', __name__, template_folder='views')

@server.route('/')
def main_route():
    """Show landing page"""

    options = {}
    return render_template("index.html", **options)

@server.route('/signup')
def signup_route():
    """Sign up page"""

    # 2.0 log in option

    options = {}
    return render_template("signup_form.html", **options)
