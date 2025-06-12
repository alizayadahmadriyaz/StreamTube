// components/ViewTracker.jsx
import { useEffect } from 'react';
import axios from 'axios';

const ViewTracker = ({ videoId}) => {
  
  // console.log(token)
  useEffect(() => {
      const result= async()=>{
      const token = localStorage.getItem('accessToken');
      try {
        const response = await axios.post(
          `http://localhost:8000/check/track/${videoId}`,
          {},
          {
            headers: {
              Authorization: `Bearer ${token}`,
              'Content-Type': 'application/json',
            },
          }
        );
        console.log('view response')
        console.log(response)
      } catch (error) {
        console.error('Failed to track view:', error);
      }
    }
    result()
  }, [videoId]);

  return null; // This component doesn't render anything
};

export default ViewTracker;
