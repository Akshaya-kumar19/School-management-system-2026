from flask import Flask, jsonify
from flask_cors import CORS
from config import Config

from routes import students, teachers, courses, enrollments, auth

app = Flask(__name__)
app.config.from_object(Config)

# Cors
CORS(app, resources={r"/api/*" : {"origins": "http://localhost:3000"}})

app.register_blueprint(students.bp, url_prefix = "/api/students")
app.register_blueprint(teachers.bp, url_prefix = "/api/teachers")
app.register_blueprint(courses.bp, url_prefix = "/api/courses")
app.register_blueprint(enrollments.bp, url_prefix = "/api/enrollments")
app.register_blueprint(auth.bp, url_prefix = "/api/auth")

@app.route("/")
def index():
    return {
        "message": "school management system",
        "version" : "1.0",
        "endpoints" : {
            'students' : '/api/students',
            "teachers" : "/api/teachers"
        }
    }


@app.route('api/health')
def health_check():
    return {"status" : "healthy", "message": "API is running"}


@app.route("/api/dashboard/stats")
def dashboard_stats():
    try:
        from models import db
        
        students_count = db.execute_query("SELECT COUNT(*) as count from students")[0]["count"]

        teachers_count = db.execute_query("SELECT COUNT(*) as count from teachers")[0]["count"]

        courses_count = db.execute_query("SELECT COUNT(*) as count from courses")[0]["count"]

        enrollments_count = db.execute_query("SELECT COUNT(*) as count from enrollments")[0]["count"]

        recent_enrollments = db.execute_query("""SELECT e.*, CONCAT(s.first_name, ' ', last_name) as student_name, c.course_name
        FROM enrollments e JOIn students s ON e.student_id = s.id
        JOIN courses c on e.course_id = c.id Order by e.created_at DESC
        LIMIT 5""")

        return jsonify({
            "total_students" : students_count,
            "total_teachers" : teachers_count,
            "total_courses" : courses_count,
            "total_enrollments" : enrollments_count,
            "recent_enrollemnts" : recent_enrollments,
        })
    except Exception as e:
        return jsonify({"error" : str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True, port=5000)