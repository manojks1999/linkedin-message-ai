from flask import Blueprint, jsonify, request, abort
# from .models import db, User
from .controllers.scrapper_controller import ScrapperController

lama_api = Blueprint('lama_api', __name__)

# Get all users


@lama_api.route('/', methods=['GET'])
def root_route():
    try:
        return jsonify({'status': True}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@lama_api.route('/linkedin/get_person', methods=['POST'])
def get_person():
    try:
        scrapper_controller = ScrapperController()
        users_data = scrapper_controller.get_person(request)
        if 'err' in users_data:
            return jsonify(users_data), 400
        return jsonify(users_data), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Get a single user by ID
@lama_api.route('/api/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = User.query.get(user_id)
    if not user:
        abort(404, description="User not found")
    return jsonify({"id": user.id, "username": user.username, "email": user.email}), 200