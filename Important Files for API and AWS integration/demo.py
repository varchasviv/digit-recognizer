from flask import Flask
import numpy
import pickle
app=Flask(__name__)

@app.route('/')
def home():
    return  "This is from Flask!!!"

if __name__ == "__main__":
    app.run()