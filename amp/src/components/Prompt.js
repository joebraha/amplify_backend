import React, { useState } from "react"; 
// importing Link from react-router-dom to navigate to  
// different end points. 
import { Link } from "react-router-dom"; 
import { useEffect } from "react";
import '../App.css';

//Put url of page to send prompt data to in action field below
const Prompt = () => { 
  return ( 
    <div className = "App"> 
    <header className = "App-header">
      <h1>Prompt-Based Generation</h1>
      <br />
        <form action="/" method="GET"> 
            <p>Please type in your song prompt below:</p>
            <input type="text"/>
        </form>
        <li> 
          {/* Endpoint to route to Home Page */} 
          <Link to="/">Return to Home</Link> {}
        </li>
      </header>
    </div> 
  ); 
}; 
  
export default Prompt; 