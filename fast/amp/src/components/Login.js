import React, { useState } from "react"; 
// importing Link from react-router-dom to navigate to  
// different end points. 
import { Link } from "react-router-dom"; 
import { useState, useEffect } from "react";
import api from './api'
import "../App.css";
  


//Todo: fill in with contact information
const Login = () => { 
  const [username, setUser] = useState("");
  const [password, setPass] = useState("");
  const result = {};

  const formSubmit = async (event) => {
    event.preventDefault();
    console.log("submitting...")
    result = await api.post('/login', {username, password});
    setUser("");
    setPass("");
    console.log(result);
  }
  const handleChangeUser = (event) => {
    setUser(event.target.value);
  }
  const handleChangePass = (event) => {
    setPass(event.target.value);
  }

  return ( 
    <div className = "App">
      <header className = "App-header">
      <h1>Login</h1> 
      <br /> 
      <form onSubmit={formSubmit}> {/* send to backend */}
            <p>Username:</p>
            <input type="text" value={username} onChange={handleChangeUser}/>
            <p>Password:</p>
            <input type="text" value={password} onChange={handleChangePass}/>
            <input type="submit" value="Submit"/>
        </form>
      <u>
        <p>amplifyb36@gmail.com</p>
      </u>
      <li> 
          {/* Endpoint to route to Home Page */} 
          <Link to="/">Return to Home</Link> {}
      </li>
      </header>
    </div> 
  ); 
}; 

export default Login;