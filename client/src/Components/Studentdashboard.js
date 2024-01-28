import React, { useState, useEffect } from 'react';

function Studentdashboard (){
  const [courses, setCourses] = useState([]);

  useEffect(() => {
    
    const fetchStudentData = async () => {
      try {
        const response = await fetch('http://127.0.0.1:5555/students/<int:id>', {
          method: 'GET',
          headers: {
            'Content-Type': 'application/json',
          },
         });

        if (!response.ok) {
          throw new Error('Failed to fetch student data');
        }

        const data = await response.json();
        setCourses(data.courses);
      } catch (error) {
        console.error('Error fetching student data:', error.message);
      }
    };

    fetchStudentData();
  }, []); 

  return (
    <div>
      <h2>Student Dashboard</h2>
      {courses.length > 0 ? (
        <table>
          <thead>
            <tr>
              <th>Course Name</th>
              <th>Grade</th>
              <th>Progress</th>
              <th>Enrollment Date</th>
            </tr>
          </thead>
          <tbody>
            {courses.map((course) => (
              <tr key={course.id}>
                <td>{course.name}</td>
                <td>{course.grade}</td>
                <td>{course.progress}%</td>
                <td>{course.enrollmentDate}</td>
              </tr>
            ))}
          </tbody>
        </table>
      ) : (
        <p>No courses available</p>
      )}
    </div>
  );
};


export default Studentdashboard;
