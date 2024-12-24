from flask import Flask, render_template, url_for, redirect # to redirect from page to page.
app = Flask(__name__) # instance of a flask web application.

@app.route('/') # should write path where we can get this function.
def index(): # function that returns home-page
    return render_template('index.html')

if __name__ == "__main__":
    app.run()

