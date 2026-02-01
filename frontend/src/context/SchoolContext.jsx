import { createContext, useContext, useState } from "react";
import {
  CoursesApi,
  dashboardAPI,
  studentsApi,
  teachersApi,
} from "../api/authApi";

const SchoolContext = createContext();

export function SchoolProvider({ children }) {
  const [students, setStudents] = useState([]);
  const [teachers, setTeachers] = useState([]);
  const [courses, setCourses] = useState([]);
  const [enrollements, setEnrollments] = useState([]);
  const [stats, setStats] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  // students
  const fetchStudents = async () => {
    try {
      setLoading(true);
      const response = await studentsApi.getAll();
      setStudents(response.data);
      setError(null);
    } catch (err) {
      setError(err.response?.data?.error || "Failed to fetch students");
    } finally {
      setLoading(false);
    }
  };

  // addStudent
  const addStudent = async (studentData) => {
    try {
      setLoading(true);
      const response = await studentsApi.create(studentData);
      await fetchStudents();
      return { success: true };
    } catch (err) {
      setError(err.response?.data?.error || "Failed to create students");
      return { success: false, error: err.response };
    } finally {
      setLoading(false);
    }
  };

  const updateStudent = async (id, studentData) => {
    try {
      setLoading(true);
      const response = await studentsApi.update(id, studentData);
      await fetchStudents();
      return { success: true };
    } catch (err) {
      setError(err.response?.data?.error || "Failed to updated students");
      return { success: false, error: err.response };
    } finally {
      setLoading(false);
    }
  };

  const deleteStudent = async (id) => {
    try {
      setLoading(true);
      const response = await studentsApi.delete(id);
      await fetchStudents();
      return { success: true };
    } catch (err) {
      setError(err.response?.data?.error || "Failed to deleted students");
      return { success: false, error: err.response };
    } finally {
      setLoading(false);
    }
  };

  // ***** teachers *******
  // students
  const fetchTeachers = async () => {
    try {
      setLoading(true);
      const response = await teachersApi.getAll();
      setTeachers(response.data);
      setError(null);
    } catch (err) {
      setError(err.response?.data?.error || "Failed to fetch students");
    } finally {
      setLoading(false);
    }
  };

  // addStudent
  const addTeacher = async (teacherData) => {
    try {
      setLoading(true);
      const response = await teachersApi.create(teacherData);
      await fetchTeachers();
      return { success: true };
    } catch (err) {
      setError(err.response?.data?.error || "Failed to create teacher");
      return { success: false, error: err.response };
    } finally {
      setLoading(false);
    }
  };

  const updateTeacher = async (id, studentData) => {
    try {
      setLoading(true);
      const response = await teachersApi.update(id, studentData);
      await fetchTeachers();
      return { success: true };
    } catch (err) {
      setError(err.response?.data?.error || "Failed to updated teachers");
      return { success: false, error: err.response };
    } finally {
      setLoading(false);
    }
  };

  const deleteTeacher = async (id) => {
    try {
      setLoading(true);
      const response = await teachersApi.delete(id);
      await fetchTeachers();
      return { success: true };
    } catch (err) {
      setError(err.response?.data?.error || "Failed to deleted teacher");
      return { success: false, error: err.response };
    } finally {
      setLoading(false);
    }
  };

  //****** courese ************** */
  const fetchCourses = async () => {
    try {
      setLoading(true);
      const response = await CoursesApi.getAll();
      setCourses(response.data);
      setError(null);
    } catch (err) {
      setError(err.response?.data?.error || "Failed to fetch students");
    } finally {
      setLoading(false);
    }
  };

  // addStudent
  const addCourse = async (data) => {
    try {
      setLoading(true);
      const response = await teachersApi.create(data);
      await fetchCourses();
      return { success: true };
    } catch (err) {
      setError(err.response?.data?.error || "Failed to create course");
      return { success: false, error: err.response };
    } finally {
      setLoading(false);
    }
  };

  // dashboard
  const fetchDashboardStats = async () => {
    try {
      const response = await dashboardAPI.getStats();
      setStats(response.data);
    } catch (err) {
      setError(err.response?.data?.error || "failed to fetch dashboard");
    }
  };

  const value = {
    students,
    teachers,
    courses,
    enrollements,
    stats,
    loading,
    error,
    fetchStudents,
    addStudent,
    updateStudent,
    deleteStudent,
    fetchTeachers,
    addTeacher,
    updateTeacher,
    deleteTeacher,
    addCourse,
    fetchCourses,
    fetchDashboardStats,
  };

  return (
    <SchoolContext.Provider value={value}>{children}</SchoolContext.Provider>
  );
}

export function useSchool() {
  return useContext(SchoolContext);
}
