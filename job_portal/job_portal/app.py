# import Flask class from flask module
from flask import Flask, render_template

# create an instance of Flask class, __name__ is special variable that evaluates to the name of the current module. If module is run directly, then it is set to "__main__".
app = Flask(__name__)


# route() decorator is used to bind a function to a URL. So whenever the home page is requested, the hello() function will be called and the output of this function will be returned to the client.
@app.route("/")
def hello():
    return render_template("home.html")


# NOTE: if the script is run directly using python interpreter, then the __name__ variable is set to __main__.
if __name__ == "__main__":
    # make the server publicly available by setting host='0.0.0.0'
    # enabling debug mode, the server will automatically reload if code changes
    app.run(debug=True, host="0.0.0.0")
