#======================================================#
# + Projet: How to use API Rest with Python and Flask  #
# + Author: Pedro Impulcetto, Adapted: Thiago Piovesan #

# + API documentation using Swagger:

# YouTube video: https://youtu.be/levz4eumJ98
#======================================================#
# Libraries importation:

from flask_restx import fields
from src.server.instance import server

#======================================================#
book = server.api.model('Book', {
    'id': fields.Integer(readOnly=True, description='The unique identifier of a book'),
    'title': fields.String(required=True, description='The title of a book', min_length=3, max_length=100),
    'author': fields.String(required=True, description='The author of a book', min_length=3, max_length=100),
})