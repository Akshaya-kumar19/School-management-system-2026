from flask import Blueprint, request, jsonify, session
from werkzeug.security import check_password_hash, generate_password_hash
from models import db

bp = Blueprint("auth", __name__)

@bp.route("/login", methods = ["POST"])
def login():
    try:
        data = request.json

        if 'username' not in data or 'password' not in data:
            return jsonify({"error": "Username and password is required"}), 400
        if data["username"] == 'admin' and data["password"] == "admin123":
            return jsonify({
                "message" : "Login successful",
                "user" : {
                    "username" : data["username"],
                    "role" : "admin"
                }
            }), 200
        else :
            return jsonify({"error" : "invalid credentials"}), 401
    except Exception as e:
        return jsonify({
            "error" : str(e)
        }), 500
    
@bp.route('/logout', methods = ["POST"])
def logout():
    """Logout endpoint"""
    return jsonify({"message" : "Logout successful"}), 200

@bp.route("/me", methods=["GET"])
def get_current_user():
    return jsonify({
        "username" : 'admin',
        "role" : "admin"
    }), 200