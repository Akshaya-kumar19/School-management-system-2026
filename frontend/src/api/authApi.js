import axios from "axios";
const API_BASE_URL = "http://localhost:5000/api";

// create axios instance
const api = axios.create({
  baseURL: API_BASE_URL,
  headers: {
    "Content-Type": "application/json",
  },
});

// students
export const studentsApi = {
  getAll: () => api.get("/students"),
  getById: (id) => api.get(`/students/${id}`),
  create: (data) => api.post("/students", data),
  update: (id, data) => api.put(`/students/${id}`, data),
  delete: (id) => api.delete(`/students/${id}`),
};

// teachers
export const teachersApi = {
  getAll: () => api.get("/teachers"),
  getById: (id) => api.get(`/teachers/${id}`),
  create: (data) => api.post("/teachers", data),
  update: (id, data) => api.put(`/teachers/${id}`, data),
  delete: (id) => api.delete(`/teachers/${id}`),
};

// teachers
export const CoursesApi = {
  getAll: () => api.get("/courses"),
  getById: (id) => api.get(`/courses/${id}`),
  create: (data) => api.post("/courses", data),
  update: (id, data) => api.put(`/courses/${id}`, data),
  delete: (id) => api.delete(`/courses/${id}`),
};

// / teachers
// export const teachersApi = {
//     getAll : () => api.get('/teachers'),
//     getById : (id) => api.get(`/teachers/${id}`),
//     create : (data) => api.post("/teachers", data),
//     update : (id, data) => api.put(`/teachers/${id}`, data),
//     delete : (id) => api.delete(`/teachers/${id}`)
// }

// Dashboard
export const dashboardAPI = {
  getStats: "/dashboard/stats",
};

// Auth

export const authAPI = {
  login: (credentials) => api.post("/auth/login", credentials),
  logout: () => api.post("/auth/logout"),
  getCurrentUser: () => api.get("/auth/me"),
};
