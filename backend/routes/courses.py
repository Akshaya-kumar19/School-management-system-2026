from flask import Blueprint, request, jsonify
from models import db
import mysql.connector

bp = Blueprint("courses", __name__)

@bp.route("" , methods=["GET"])
def get_courses():
    try:

        query = """SELECT c.*, CONCAT(t.first_name, ' ', t.last_name) as teacher_name FROM courses c LEFT JOIN teachers t ON c.teacher_id = t.id ORDER BY c.created_at DESC"""

        courses = db.execute_query(query)
        return jsonify(courses), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
@bp.route('/<int:id>', methods = ['GET'])
def get_course(id):
    try:

        # get course details
        course_query = """SELECT c.*, CONCAT(t.first_name, ' ', t.last_name) as teacher_name FROM courses c LEFT JOIN teachers t ON c.teacher_id = t.id WHERE c.id = %s"""

        courses = db.execute_query(course_query, (id,))

        if not courses:
            return jsonify({"error": "course does not exist"}), 404
        
        course = courses[0]

        # get enrolled students
        students_query = """SELECT s.id, s.student_id, s.first_name, s.last_name, e.grade, e.status FROM enrollments e JOIN students s ON e.student_id = s.id where e.course_id = %s"""

        students = db.execute_query(students_query, (id, ))
        course["enrolled_students"] = students
        course["enrollment_count"] = len(students)

        return jsonify(course), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
@bp.route("", methods = ["POST"])
def create_teacher():
    try : 
        data = request.json

        required_fields = ["course_code", "course_name", "credits"]
        for field in required_fields:
            if field not in data:
                return jsonify({"error": f"{field} is required"}), 400
            
        query = """INSERT INTO courses course_code, course_name, description, credits, teacher_id, capacity, semester VALUES (%s, %s, %s, %s, %s, %s, %s)"""

        params = (
            data["course_code"],
            data["course_name"],
            data["description"],
            data["credits"],
            data["teacher_id"],
            data["capacity"],
            data["semester"]
        )

        course_id = db.execute_query(query, params, fetch=False)
        return jsonify({"message": "course created successfully", "id": course_id}), 201
    except Exception as e :
        return jsonify({"error": str(e)}), 500
    
@bp.route("", methods = ["PUT"])
def update_course(id):
    try : 
        data = request.json

            
        query = """UPDATE courses set  course_code = %s, course_name = %s, description = %s, credits = %s, teacher_id = %s, capacity = %s, semester = %s WHERE id = %s"""

        params = (
            data["course_code"],
            data["course_name"],
            data["description"],
            data["credits"],
            data["teacher_id"],
            data.get("capacity", 30),
            data["semester"],
            id
        )

        course_id = db.execute_query(query, params, fetch=False)
        return jsonify({"message": "course updated successfully"}), 200
    except Exception as e :
        return jsonify({"error": str(e)}), 500
    
@bp.route("/<int:id>", methods=["DELETE"])
def delete_course(id):
    try :
        query = "DELETE FROM courses WHERE id = %s"
        db.execute_query(query, (id,), fetch=False)

        return jsonify({"message": "course deleted successfully", }), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500