import React, { useState, useEffect } from 'react';

function Courses (){
  const [courses, setCourses] = useState([]);
  const [selectedCourse, setSelectedCourse] = useState(null);

  useEffect(() => {
    // Fetch the list of available courses with instructor details from the backend
    const fetchCourses = async () => {
      try {
        const response = await fetch('http://127.0.0.1:5555/courses');
        if (!response.ok) {
          throw new Error('Failed to fetch courses');
        }

        const data = await response.json();
        setCourses(data);
      } catch (error) {
        console.error('Error fetching courses:', error.message);
      }
    };

    fetchCourses();
  }, []);

  const handleEnroll = async () => {
    if (!selectedCourse) {
      console.error('No course selected for enrollment');
      return;
    }

    try {
      const response = await fetch('http://127.0.0.1:5555/enrollments', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ course_id: selectedCourse.id }),
      });

      if (!response.ok) {
        throw new Error('Enrollment failed');
      }

      const data = await response.json();
      console.log('Enrollment successful:', data);

      // Handle any UI updates or redirection after successful enrollment
    } catch (error) {
      console.error('Error during enrollment:', error.message);
    }
  };

  return (
    <div>
      <h2>Course Browser</h2>
      <ul>
        {courses.map((course) => (
          <li key={course.id}>
            <strong>{course.title}</strong> - {course.description}<br />
            {course.instructor && (
              <span>Instructor: {course.instructor.instructor_fname} {course.instructor.instructor_lname}</span>
            )}
            <button onClick={() => setSelectedCourse(course)}>Enroll</button>
          </li>
        ))}
      </ul>
      {selectedCourse && (
        <div>
          <h3>Selected Course: {selectedCourse.title}</h3>
          {selectedCourse.instructor && (
            <p>Instructor: {selectedCourse.instructor.instructor_fname} {selectedCourse.instructor.instructor_lname}</p>
          )}
          <button onClick={handleEnroll}>Enroll in Course</button>
        </div>
      )}
    </div>
  );
};

export default Courses;
