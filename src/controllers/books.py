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

from urllib import response
from flask import Flask
from flask_restx import Api, Resource

from src.server.instance import server
from src.models.books import book
#======================================================#
# Endpoint creation:
app, api = server.app, server.api

#======================================================#
# Create a books list to simulate a database:
books_db = [
    {'id': 1, 'title': 'The Lord of the Rings', 'author': 'J.R.R. Tolkien', 'year': 1954},
    {'id': 2, 'title': 'The Hobbit', 'author': 'J.R.R. Tolkien', 'year': 1937},
    {'id': 3, 'title': 'The Fellowship of the Ring', 'author': 'J.R.R. Tolkien', 'year': 1954},
]

#======================================================#
# Import Resource because is responsible for get and post methods:


@api.route('/books')
class Booklist(Resource):
    
    @api.marshal_list_with(book)
    def get(self, ):
        return books_db     # In this part we should request the database
                            # but in this case we will return a list
    
    @api.expect(book, validate=True)
    @api.marshal_with(book)
    def post(self, ):
        response = api.payload
        books_db.append(response)
        
        return response, 200    # First information is the payload, second is the status code
#======================================================#
