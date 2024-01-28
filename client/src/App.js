import React from "react";
import {BrowserRouter as Router, Routes, Route} from 'react-router-dom'
import RegistrationForm from "./Components/Registration";
import Studentdashboard from "./Components/Studentdashboard";
import Courses from "./Components/Courses";
import LoginForm from "./Components/Login";

function App() {
  return (
    <Router>
      <div>
      <h1>Mach LMS</h1>
      <div>
      <Routes>
        <Route path="/login" element = {<LoginForm />} />
        <Route path="/register" element ={<RegistrationForm />} />
        <Route path="/student-dashboard" Component = {<Studentdashboard />} />
        <Route path="/courses" element = {<Courses />} />
      </Routes>
      </div>
      </div>
    </Router>
  );
}

export default App;
