import { useEffect, useState } from "react";
import { useSchool } from "../../context/SchoolContext";
import { useNavigate } from "react-router-dom";

function StudentsList() {
  const { students, loading, fetchStudents, deleteStudents } = useSchool();

  const navigate = useNavigate();

  const [searchTerm, setSearchTerm] = useState("");

  useEffect(() => {
    fetchStudents();
  }, []);

  const handleDelete = async (id) => {
    if (window.confirm("Are you sure you want to delete this student ?")) {
      const result = await deleteStudents(id);
      if (result.success) {
        alert("student deleted succesfully");
      }
    }
  };

  const filteredStudents = students.filter(
    (student) =>
      student.first_name.toLowerCase.includes(searchTerm.toLowerCase) ||
      student.last_name.toLowerCase.includes(searchTerm.toLowerCase) ||
      student.student_id.includes(searchTerm),
  );

  if (loading) return <div className="loading">Loading</div>;

  return (
    <div className="students-list">
      <div className="page-header">
        <h1>Student Management</h1>

        <button
          className="btn btn-primary"
          onClick={() => navigate("/students/new")}
        >
          Add student
        </button>
      </div>

      <div className="search-box">
        <input
          type="text"
          placeholder="search by name or ID"
          value={searchTerm}
          onChange={(e) => setSearchTerm(e.target.value)}
          className="search-input"
        />
      </div>

      <div className="table-container">
        <table className="data-table">
          <thead>
            <tr>
              <th>Student ID</th>
              <th>Name</th>
              <th>Email</th>
              <th>Phone</th>
              <th>Gender</th>
              <th>Enrollment date</th>
              <th>Actions</th>
            </tr>
          </thead>
          <tbody>
            {filteredStudents.map((student) => (
              <tr key={student.id}>
                <td>{student.student_id}</td>
                <td>
                  {student.first_name} {student.last_name}
                </td>
                <td>{student.email}</td>
                <td>{student.phone} || N/A</td>
                <td>{student.gender}</td>
                <td>{student.enrollment_date}</td>
                <td className="actions">
                  <button
                    className="btn btn-sm btn-info"
                    onClick={() => navigate(`/students/${student.id}`)}
                  >
                    View
                  </button>
                  <button
                    className="btn btn-sm btn-warning"
                    onClick={() => navigate(`/students/edit/${student.id}`)}
                  >
                    Edit
                  </button>
                  <button
                    className="btn btn-sm btn-danger"
                    onClick={() => handleDelete(student.id)}
                  >
                    Delete
                  </button>
                </td>
              </tr>
            ))}
          </tbody>
        </table>

        {filteredStudents.length === 0 && (
          <div className="no-data">No students found</div>
        )}

        <div className="stats-footer">
          <p>Total students : {filteredStudents.length}</p>
        </div>
      </div>
    </div>
  );
}
