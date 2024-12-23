from flask import Flask, url_for, redirect # to redirect from page to page.
app = Flask(__name__) # instance of a flask web application.

@app.route('/') # should write path where we can get this function.
def home(): # function that returns home-page
    return "here should be html"

@app.route('/<name>') # root with par name in <>.
def user(name):
    return f"Hello {name}" # format string.

@app.route('/admin') # its a decorator in python.
def admin():
    return redirect(url_for("home"))

# to start a web cite.
if __name__ == "__main__":
    app.run()
