from flask import Flask, jsonify, request
from controllers import cv_proctoring_controller, nlp_processing_controller

app = Flask(__name__)

# Register Blueprints
app.register_blueprint(cv_proctoring_controller.bp, url_prefix='/cv')
app.register_blueprint(nlp_processing_controller.bp, url_prefix='/nlp')

@app.route('/')
def index():
    return "AI/ML Service is running."

@app.route('/health')
def health_check():
    return jsonify({"status": "healthy"}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)