# importing necessary modules
from flask import Flask
# creating a python flask application
app=Flask(__name__)

@app.route("/")
def index():
    return "<h1>hello world</h1>"
# initialize server
if __name__ == '__main__':
    app.run(debug=True)



