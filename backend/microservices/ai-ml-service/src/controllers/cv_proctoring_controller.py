from flask import Blueprint, jsonify, request
from services import cv_service

bp = Blueprint('cv_proctoring', __name__)

@bp.route('/analyze_frame', methods=['POST'])
def analyze_frame():
    """
    Analyzes a single video frame for proctoring purposes.
    Expects a JSON payload with an 'image' field containing a base64 encoded image.
    """
    if not request.json or 'image' not in request.json:
        return jsonify({"error": "Missing image data"}), 400

    image_data = request.json['image']

    try:
        # Placeholder for CV service call
        analysis_result = cv_service.analyze_proctoring_frame(image_data)
        return jsonify(analysis_result), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@bp.route('/detect_fraud', methods=['POST'])
def detect_fraud():
    """
    Analyzes a sequence of events or frames to detect potential fraud.
    """
    # Placeholder logic
    event_data = request.json.get('events', [])
    if not event_data:
        return jsonify({"error": "No events provided"}), 400

    result = {
        "fraud_detected": False,
        "reason": "No suspicious patterns found in the provided events."
    }

    # Example of simple rule-based detection
    if len(event_data) > 5:
        result = {
            "fraud_detected": True,
            "reason": "Multiple suspicious events detected.",
            "confidence": 0.85
        }

    return jsonify(result), 200