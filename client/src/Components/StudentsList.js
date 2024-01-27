import React, { useState, useEffect } from 'react';

const StudentsList = () => {
  const [students, setStudents] = useState([]);
  const [formData, setFormData] = useState({
    firstname: '',
    lastname: '',
    email: '',
  });

  const fetchStudents = async () => {
    try {
      const response = await fetch('http://127.0.0.1:5555/students');
      const data = await response.json();
      setStudents(data);
    } catch (error) {
      console.error('Error fetching students:', error);
    }
  };

  const handleInputChange = (e) => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  const handleAddStudent = async () => {
    try {
      const response = await fetch('http://127.0.0.1:5555/students', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(formData),
      });

      if (response.ok) {
        const data = await response.json();
        console.log('Student added successfully. Student ID:', data.student_id);
        setFormData({ firstname: '', lastname: '', email: '' });
        fetchStudents();
      } else {
        const errorData = await response.json();
        console.error('Error adding student:', errorData.message);
      }
    } catch (error) {
      console.error('Error adding student:', error);
    }
  };

  useEffect(() => {
    fetchStudents();
  }, []);

  return (
    <div>
      <h1>Students List</h1>
      <ul>
        {students.map((student) => (
          <li key={student.id}>{`${student.firstname} ${student.lastname} - ${student.email}`}</li>
        ))}
      </ul>
      <h2>Add Student</h2>
      <div>
        <label>First Name:</label>
        <input type="text" name="firstname" value={formData.firstname} onChange={handleInputChange} />
      </div>
      <div>
        <label>Last Name:</label>
        <input type="text" name="lastname" value={formData.lastname} onChange={handleInputChange} />
      </div>
      <div>
        <label>Email:</label>
        <input type="text" name="email" value={formData.email} onChange={handleInputChange} />
      </div>
      <button onClick={handleAddStudent}>Add Student</button>
    </div>
  );
};

export default StudentsList;
