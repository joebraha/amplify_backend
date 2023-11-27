import React, { useState } from "react"; 
// importing Link from react-router-dom to navigate to  
// different end points. 
import { Link } from "react-router-dom"; 
import { useEffect } from "react";
import "../App.css";

const Account = () => { 
  return ( 
    <div className="App">
      <header className="App-header"> 
      <h1>Account</h1> 
      <br /> 
      <ul> 
        <li> 
          {/* Endpoint to route to Home Page */} 
          <Link to="/">Return to Home</Link> {}
        </li>
        <li> 
          {/* Endpoint to route to Home component */} 
          <Link to="/">Home</Link> 
        </li> 
        <li> 
          {/* Endpoint to route to Login component */} 
          <Link to="/login">Login</Link> 
        </li> 
        <li> 
          {/* Endpoint to route to Saved Playlists component */} 
          <Link to="/playlists">See Saved Playlists</Link>
           
        </li>
        {/* expand to include: friends, ...  */}

          
      </ul>
      </header> 
    </div> 
  ); 
}; 
  
export default Account; 