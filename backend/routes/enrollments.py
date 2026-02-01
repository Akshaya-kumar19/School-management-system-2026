# from flask import Blueprint, request, jsonify
# from models import db
# import mysql.connector

# bp = Blueprint("enrollments", __name__)

# @bp.route("" , methods=["GET"])
# def get_enrollments():
#     try:
#         query = """SELECT e.id, e.enrollment_date, e.grade, e.status, s.student_id, CONCAT(s.first_name, ' ', last_name) as student_name, c.course_code, c.course_name 
#         FROM enrollments e JOIN students ON e.student_id = s.id
#         JOIN courses c ON e.course_id = c.id 
#         ORDER BY e.created_at DESC"""

#         enrollments = db.execute_query(query)

#         for 