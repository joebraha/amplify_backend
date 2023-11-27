import React, { useState } from "react"; 
// importing Link from react-router-dom to navigate to  
// different end points. 
import { Link } from "react-router-dom"; 
import { useEffect } from "react";
import "../App.css";
  


//Todo: fill in with contact information
const ContactUs = () => { 


  return ( 
    <div className = "App">
      <header className = "App-header">
      <h1>Contact Us</h1> 
      <br /> 
      <p>Contact us below at:</p>
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

export default ContactUs;