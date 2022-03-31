#======================================================#
# + Projet: How to use API Rest with Python and Flask  #
# + Author: Pedro Impulcetto, Adapted: Thiago Piovesan #

# + Flask: Flask is a microframework for Python. 
# It's a small and simple framework that makes it easy 
# to build simple web applications.

# Module: main.py --> Library.

# YouTube video: https://youtu.be/levz4eumJ98
#======================================================#

# Libraries importation:

from src.server.instance import server

# Now we have to import all the controllers we create:
from src.controllers.books import *

#======================================================#
# Create a Flask application:
server.run()

#======================================================#
# Route Creation:


#======================================================#
