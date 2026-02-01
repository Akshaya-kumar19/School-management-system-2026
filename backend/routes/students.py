
from flask import Blueprint, request, jsonify
from models import db
import mysql.connector

bp = Blueprint("students", __name__)

# get all 
@bp.route("", methods=["GET"])
def get_students():
    try:
        query = """
SELECT id, student_id, first_name, last_name, email, phone, date_of_birth,  gender, address, enrollment_date FROM students order by created_at desc"""
        students = db.execute_query(query)

        for student in students:
            if student["date_of_birth"]:
                student["date_of_birth"] = student["date_of_birth"].strftime("%d-%m-%Y")
            if student["enrollment_date"]:
                student["enrollment_date"] = student["enrollment_date"].strftime("%d-%m-%Y")

        return jsonify(students), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# get student  
@bp.route('/<int:id>', methods = ['GET'])
def get_student():
    try:
        query = "select * from students where id = %s"
        students = db.execute_query(query, (id,))

        if not students :
            return jsonify({'error': "student not found"}), 404
        student = student[0]

        if student["date_of_birth"]:
            student["date_of_birth"] = student["date_of_birth"].strftime("%d-%m-%Y")
        if student["enrollment_date"]:
            student["enrollment_date"] = student["enrollment_date"].strftime("%d-%m-%Y")

        return jsonify(student), 200
    except Exception as e:
        return jsonify({"Error": str(e)}), 500


    
# post student
@bp.route("", methods = ["POST"])
def create_student():
    try : 
        data = request.json

        # validation
        required_fields = ["student_id", "first_name", "last_name", "email"]
        for field in required_fields:
            if field not in data:
                return jsonify({"error": f"{field} is required"}), 400
            
        query = """
INSERT INTO students (student_id, first_name, last_name, email, phone, date_of_birth,  gender, address) VALUES (%s, %s, %s,%s,%s,%s,%s,%s)"""
        params = (data["student_id"], data["first_name"], data["last_name"],data["email"], data["phone"], data["date_of_birth"],data["gender"], data["address"])

        student_id = db.execute_query(query, params, fetch=False)

        return jsonify({"message": "Student created successfully", "id": student_id}), 201
    except mysql.connector.IntegrityError as e : 
        if "Duplicate entry" in str(e):
            return jsonify({"error": "student id or email already exists"}), 409
        return jsonify({"error": str(e)}), 500
    except Exception as e :
        return jsonify({"error": str(e)}), 500
    
@bp.route('/<int:id>', methods = ["PUT"])
def update_student(id):
    try : 
        data = request.json

        query = """
UPDATE students SET first_name = %s, last_name = %s, email = %s, phone = %s, date_of_birth = %s,  gender = %s, address = %s WHERE id = %s"""
        params = ( data["first_name"], data["last_name"],data["email"], data["phone"], data["date_of_birth"],data["gender"], data["address"], id)

        db.execute_query(query , params, fetch= False)

        return jsonify({"message": "Student updated successfully", }), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    

# delete student
@bp.route("/<int:id>", methods=["DELETE"])
def delete_student(id):
    try :
        query = "DELETE FROM students WHERE id = %s"
        db.execute_query(query, (id,), fetch=False)

        return jsonify({"message": "Student deleted successfully", }), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500