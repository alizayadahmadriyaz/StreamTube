import React from 'react';
import { Link } from 'react-router-dom';

const Navbar = () => (
  <nav className="bg-white shadow p-4 flex justify-between items-center">
    <Link to="/" ><button type="submit" >StreamTube</button></Link>
    <div>
      <Link to="/Register" className="text-gray-700 hover:text-red-500">Register</Link>
    </div>
  </nav>
);

export default Navbar;