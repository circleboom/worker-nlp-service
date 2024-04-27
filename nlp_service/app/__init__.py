import logging
from flask import Flask

def create_app():
    app = Flask(__name__)
    
    # Set up basic logging
    logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

    # Example of adding a simple log statement
    logging.info("Starting the nlp_service")
    
    # Import and setup routes from nlp_service
    from .nlp_service import setup_routes
    setup_routes(app)

    return app
