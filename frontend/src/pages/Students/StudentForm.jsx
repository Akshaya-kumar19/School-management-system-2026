import { useNavigate, useParams } from "react-router-dom";
import { useSchool } from "../../context/SchoolContext";
import { useEffect, useState } from "react";
import { studentsApi } from "../../api/authApi";

function StudentForm() {
  const { id } = useParams();
  const navigate = useNavigate();
  const { addStudent, updateDelete } = useSchool();
  const isEditMode = Boolean(id);

  const [formData, setFormData] = useState({
    student_id: "",
    first_name: "",
    last_name: "",
    email: "",
    phone: "",
    date_of_birth: "",
    gender: "Male",
    address: "",
  });

  const [errors, setErrors] = useState({});
  const [loading, setLoading] = useState(false);

  useEffect(() => {
    if (isEditMode) {
      loadStudent();
    }
  });

  const loadStudent = async () => {
    try {
      setLoading(true);
      const response = await studentsApi.getById(id);
      setFormData(response.data);
    } catch (err) {
      alert("Failed to load student");
    } finally {
      setLoading(false);
    }
  };

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData((prev) => ({
      ...prev,
      [name]: value,
    }));

    if (errors[name]) {
      setErrors((prev) => ({
        ...prev,
        [name]: "",
      }));
    }
  };

  const validate = () => {
    const newErrors = {}

    if(!formData.student_id.trim()){
        newErrors.student_id = "student id is required"
    }
    if(!formData.first_name.trim()){
        newErrors.first_name = "first name is required"
    }
    if(!formData.last_name.trim()){
        newErrors.last_name = "last name id is required"
    }
    if(!formData.email.trim()){
        newErrors.email = "email is required"
    }

    return newErrors
  }

  const handleSubmit = async (e) => {
    e.preventDefault()

    const newErrors = validate();
    if (Object.keys(newErrors))
  }
}
