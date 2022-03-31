#======================================================#
# + Projet: How to use API Rest with Python and Flask  #
# + Author: Pedro Impulcetto, Adapted: Thiago Piovesan #

# + Flask: Flask is a microframework for Python. 
# It's a small and simple framework that makes it easy 
# to build simple web applications.

# + Flask_restplus: Flask_restplus is a Python library 
# that makes it easy to create RESTful APIs in Flask.

# YouTube video: https://youtu.be/levz4eumJ98
#======================================================#
# Libraries importation:

from flask import Flask
from flask_restx import Api

#======================================================#
# Create a class that will be used to create the Flask application:

class Server:
    def __init__(self, ):
        self.app = Flask(__name__)
        self.api = Api(self.app, 
            version='1.0', 
            title='Simple Book API', 
            description='A simple Book API', 
            doc='/docs'             # Documentation URL
        )
    
    # Turn debug to False to production mode:    
    def run(self, ):
        self.app.run(
            debug=True              # Debug mode    
        )
        
#======================================================#
# Create the server:

server = Server()