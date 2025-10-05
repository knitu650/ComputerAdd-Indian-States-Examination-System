from flask import Blueprint, jsonify, request
from services import nlp_service

bp = Blueprint('nlp_processing', __name__)

@bp.route('/generate_questions', methods=['POST'])
def generate_questions():
    """
    Generates questions based on a given context or topic.
    Expects a JSON payload with a 'text' field.
    """
    if not request.json or 'text' not in request.json:
        return jsonify({"error": "Missing text for question generation"}), 400

    context = request.json['text']
    num_questions = request.json.get('count', 5)

    try:
        # Placeholder for NLP service call
        questions = nlp_service.generate_questions_from_text(context, num_questions)
        return jsonify({"questions": questions}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@bp.route('/evaluate_answer', methods=['POST'])
def evaluate_answer():
    """
    Evaluates a user's answer against a reference answer.
    Expects 'user_answer' and 'reference_answer' fields.
    """
    if not request.json or 'user_answer' not in request.json or 'reference_answer' not in request.json:
        return jsonify({"error": "Missing required fields for answer evaluation"}), 400

    user_answer = request.json['user_answer']
    reference_answer = request.json['reference_answer']

    try:
        # Placeholder for NLP service call
        evaluation = nlp_service.evaluate_answer_similarity(user_answer, reference_answer)
        return jsonify(evaluation), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500