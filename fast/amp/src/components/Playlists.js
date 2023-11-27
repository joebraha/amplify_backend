import React, { useState } from "react"; 
// importing Link from react-router-dom to navigate to  
// different end points. 
import { Link } from "react-router-dom"; 
import { useEffect } from "react";
  


//TODO: Fill with saved playlists
const Playlists = () => { 


  return ( 
    <div> 
      <h1>Saved Playlists</h1> 
      <br /> 
      <ul>
        
      </ul>
      <li> 
          {/* Endpoint to route to Home Page */} 
          <Link to="/">Return to Home</Link> {}
      </li>
    </div> 
  ); 
}; 
  
export default Playlists; 