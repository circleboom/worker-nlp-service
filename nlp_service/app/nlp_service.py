# filename: nlp_service.py
from flask import request, jsonify
import spacy
import logging

def setup_routes(app):
    @app.route('/')
    def home():
        return 'Home Page', 200

    @app.route('/extract_keywords', methods=['POST'])
    def extract_keywords():
        logging.info("Received request for keyword extraction")
        try:
            # Load the spaCy model
            nlp = spacy.load('xx_ent_wiki_sm')  # Supports multiple languages

            # Extract data from request
            data = request.json
            text = data['text']

            logging.debug("Extracting keywords from text: %s", text)

            # Process text through spaCy NLP model
            doc = nlp(text)
            keywords = [token.text for token in doc if not token.is_stop and not token.is_punct]

            logging.info('Returning keywords as a JSON response: %s', keywords)
            
            # Return keywords as a JSON response
            return jsonify(keywords=keywords)
        except Exception as e:
            logging.error(f"Error during keyword extraction: {str(e)}")
            return jsonify(error=str(e)), 500