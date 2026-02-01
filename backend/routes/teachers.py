from flask import Blueprint, request, jsonify
from models import db
import mysql.connector

bp = Blueprint("teachers", __name__)

@bp.route("" , methods=["GET"])
def get_teachers():
    try:
        # `teacher_id``first_name``last_name``phone``subject``qualification``experience_years``salary``hire_date`
        query = """SELECT id, teacher_id, first_name, last_name, email, phone, subject, qualification, experience_years, salary, hire_date FROM teachers ORDER BY created_at DESC"""

        teachers = db.execute_query(query)

        for teacher in teachers :
            if teacher["hire_date"]:
                teacher["hire_date"] = teacher["hire_date"].strftime("%d-%m-%Y")

        return jsonify(teachers), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
@bp.route('/<int:id>', methods = ['GET'])
def get_teacher(id):
    try:
        # `teacher_id``first_name``last_name``phone``subject``qualification``experience_years``salary``hire_date`
        query = """SELECT * FROM teachers WHERE id = %s"""

        teacher = db.execute_query(query, (id,))

        if not teacher : 
            return jsonify({"error": "teacher does not exist"}), 404
        teacher = teacher[0]
        if teacher["hire_date"]:
            teacher["hire_date"] = teacher["hire_date"].strftime("%d-%m-%Y")

        return jsonify(teacher), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    

@bp.route("", methods = ["POST"])
def create_teacher():
    try : 
        data = request.json

        required_fields = ["first_name", "last_name", "email", "subject"]

        for field in required_fields:
            if field not in data:
                return jsonify({"error": f"{field} is required"}), 400
            
        query = """INSERT INTO teachers (teacher_id, first_name, last_name, email, phone, subject, qualification, experience_years, salary) values (%s, %s, %s, %s, %s, %s, %s, %s, %s)"""

        params = (data["teacher_id"], data["first_name"], data["last_name"],data["email"], data["phone"], data["subject"],data["qualification"], data["experience_years"], data["salary"])

        teacher_id = db.execute_query(query, params, fetch=False)

        return jsonify({"message": "Teacher created successfully", "id": teacher_id}), 201
    except mysql.connector.IntegrityError as e : 
        if "Duplicate entry" in str(e):
            return jsonify({"error": "teacher id or email already exists"}), 409
        return jsonify({"error": str(e)}), 500
    except Exception as e :
        return jsonify({"error": str(e)}), 500
    


@bp.route('/<int:id>', methods = ["PUT"])
def update_teacher(id):
    try : 
        data = request.json

        query = """
UPDATE teachers SET first_name = %s, last_name = %s, email = %s, phone = %s, subject = %s,  qualification = %s, experience_years = %s, salary= %s WHERE id = %s"""
        params = ( data["first_name"], data["last_name"],data["email"], data["phone"], data["subject"],data["qualification"], data["experience_years"], data["salary"], id)

        db.execute_query(query , params, fetch= False)

        return jsonify({"message": "teacher updated successfully", }), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    

# delete teacher
@bp.route("/<int:id>", methods=["DELETE"])
def delete_teacher(id):
    try :
        query = "DELETE FROM teachers WHERE id = %s"
        db.execute_query(query, (id,), fetch=False)

        return jsonify({"message": "teacher deleted successfully", }), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500