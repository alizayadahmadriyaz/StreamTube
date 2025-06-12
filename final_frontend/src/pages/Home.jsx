import React, { useEffect, useState } from 'react';
import axios from 'axios';
import { Link } from 'react-router-dom';

const Home = () => {
  const [videos, setVideos] = useState([]);

//   const URL='/music_player/streaming'
  useEffect(() => {
    axios.get('http://localhost:8000/start/videos/')
      .then(res => setVideos(res.data))
      .catch(err => console.error(err));
  }, []);
  // console.log(URL+videos[0]['thumbnail'])
//   const UU=URL+;
  return (
    <div className="p-4 grid grid-cols-1 sm:grid-cols-2 md:grid-cols-5 gap-8 max-w-10xl ">
    {/* <img src={UU} className="w-full h-48 object-cover"/> */}
      {videos.map(video => (
        <div className='bg-white shadow rounded overflow-hidden'>
        <Link to={`/video/${video.id}`} key={video.id}>
          <img src={`http://localhost:8000/${video.thumbnail}`} alt={video.title} className="w-full h-48 object-cover"/>
          {/* console.log(URL+video.thumbnail) */}
          <div className="p-2">
            <h2 className="font-semibold">{video.title}</h2>
            <p className="text-sm text-gray-500">{video.views} views</p>
          </div>
        </Link>
        </div>
      ))}
    </div>
  );
};

export default Home;
