import { AuthContext } from "./context/AuthContext";
import * as React from "react";
import { useState, useEffect, useRef } from 'react'
import { BrowserRouter as Router, Route, Routes, Link, Outlet} from 'react-router-dom';
import Login from './pages/Login'
import Signup from './pages/Signup'
import Home from './pages/Home'
import Testing from "./components/Testing";


export default function App() {
  const [authToken, setAuthToken] = useState(null);
  const [formData, setFormData] = useState({ email: '', password: '' });
  const [ads, setAds] = useState([]);

  const inputRef = useRef(null);

  const handleToken = (token) => {
    setFormData({ email: '', password: '' });
    setAuthToken(token);
  };

  const sharedState = {
    formData,
    setFormData,
    authToken,
    setAuthToken,
    handleToken,
  };
  
  const handleInputChange = (e) => {
    const { name, value } = e.target;
    setFormData({
      ...formData,
      [name]: value,
    });
    if (inputRef.current) {
      inputRef.current.focus();
    }
  };

useEffect(() => {
  const token = localStorage.getItem('authToken')
  if (token && !authToken) {
    handleToken(token)
  }
}, [])

  return (
    <AuthContext.Provider value={sharedState}>
      <Router>
        <Routes>
          <Route path='/' element={<Login handleToken={handleToken} handleInputChange={handleInputChange}/>}/>
          <Route path='/signup' element={<Signup handleInputChange={handleInputChange} formData={formData} />}/>
          <Route path='/home' element={<Home />}/>
          <Route path='/testing' element={<Testing />}/>
        </Routes>
      </Router> 
    </AuthContext.Provider>
  );
}
