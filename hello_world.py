#======================================================#
# + Projet: How to use API Rest with Python and Flask  #
# + Author: Pedro Impulcetto, Adapted: Thiago Piovesan #

# + Flask: Flask is a microframework for Python. 
# It's a small and simple framework that makes it easy 
# to build simple web applications.

# Module: main.py --> Hello world.

# YouTube video: https://youtu.be/levz4eumJ98
#======================================================#

# Libraries importation:

from flask import Flask
#======================================================#
# Create a Flask application:
app = Flask(__name__)       # __name__ is the name of the current module


#======================================================#
# Route Creation:
@app.route('/')
def hello_world():
    return 'Hello, World!'

#======================================================#
