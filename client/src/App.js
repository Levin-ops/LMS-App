import React,{ useState, useEffect } from 'react';
import Login from './Components/Login';

function App() {
    const [user, setUser] = useState(null)

    useEffect(()=>{
      fetch("/check-session").then((response) => {
        if (response.ok){
          response.json() .then((user) => setUser(user))
        }
      });
    }, []);
 
    if(user){
      return <h2>Welcome, {user.email}</h2>
    }else{
      return <Login onLogin={setUser}/>
    }
}

export default App;
