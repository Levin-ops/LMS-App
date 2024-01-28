import React,{ useState, useEffect } from 'react';
import Login from './Components/Login';
import Navbar from './Components/Navbar';
import RegistrationForm from './Components/Registration';
import Studentdashboard from './Components/Studentdashboard';


function App() {

  return (
      <>
      <h1>Mach LMS</h1>
        <Login />
        <RegistrationForm />
        <Studentdashboard />
      </>
  )

  
}

export default App;
