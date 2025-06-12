import React, { useState } from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import Navbar from './components/Navbar';
import Home from './pages/Home';
import Register from './components/Register';
import Login from './components/login';
import VideoDetail from './pages/VideoDetail';

function App() {
  const [loginopen,setloginopen]=useState(true);
  return (
    
    <Router>
      <div className="bg-black min-h-screen text-white">
      <Navbar setloginopen={setloginopen} loginopen={loginopen}/>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/video/:id" element={<VideoDetail />} />
        <Route path="/Register" element={<Register />} />
        <Route path="/Login" element={<Login setloginopen={setloginopen}/>} />
      </Routes>
      </div>
    </Router>

  );

}

export default App;