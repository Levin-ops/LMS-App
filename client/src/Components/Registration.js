import React, { useState } from 'react';

function RegistrationForm (){
  const [formData, setFormData] = useState({
    firstname: '',
    lastname: '',
    email: '',
    password: '',
    usertype: 'student', 
    bio: '',
    specialization: '',
    experience : '',
  });

  function handleChange(event){
    const { name, value } = event.target;
    setFormData({
      ...formData,
      [name]: value,
    });
  };

  const handleSubmit = async (event) => {
    event.preventDefault();

    try {
      const response = await fetch('http://127.0.0.1:5555/register', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(formData),
      });

      if (!response.ok) {
        throw new Error('Registration failed');
      }
      window.location.href = '/login'
      console.log('Registration successful:');
    } 
    
    catch (error) {
      console.error('Error during registration:', error.message);
    }
  };

  return (
    <div>
      <h2>Registration Form</h2>
      <form onSubmit={handleSubmit}>
        <label>
          First Name:
          <input type="text" name="firstname"value={formData.firstname} onChange={handleChange}/>
        </label>
        
        <br />

        <label>
          Last Name:
          <input type="text" name="lastname" value={formData.lastname} onChange={handleChange}/>
        </label>
        <br />

        <label>
          Email:
          <input
            type="email"
            name="email"
            value={formData.email}
            onChange={handleChange}
          />
        </label>
        <br />

        <label>
          Password:
          <input
            type="password"
            name="password"
            value={formData.password}
            onChange={handleChange}
          />
        </label>
        <br />

        <label>
          User Type:
          <select name="usertype" value={formData.usertype} onChange={handleChange}>
            <option value="student">Student</option>
            <option value="instructor">Instructor</option>
          </select>
        </label>
        <br />

        {formData.usertype === 'instructor' && (
          <>
            <label>
              Bio:
              <input
                type="text"
                name="bio"
                value={formData.bio}
                onChange={handleChange}
              />
            </label>
            <br />
          </>
        )}

        {formData.usertype === 'instructor' && (
          <>
            <label>
              Specialization:
              <input
                type="text"
                name="specialization"
                value={formData.specialization}
                onChange={handleChange}
              />
            </label>
            <br />
          </>
        )}

        {formData.usertype === 'instructor' && (
          <>
            <label>
              Experience:
              <input
                type="text"
                name="experience"
                value={formData.experience}
                onChange={handleChange}
              />
            </label>
            <br />
          </>
        )}  

        <button type="submit">Register</button>
      </form>
    </div>
  );
};

export default RegistrationForm;
