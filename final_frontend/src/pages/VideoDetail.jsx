import React, { useEffect, useState } from 'react';
import { useParams } from 'react-router-dom';
import axios from 'axios';
import ViewTracker from '../components/ViewTracker'
const VideoDetail = () => {
  const { id } = useParams();
  const [video, setVideo] = useState(null);
  const [commentText, setCommentText] = useState('');
  const [comments, setComments] = useState([]);
  const [error, setError] = useState(null);
  const [currentViews, setCurrentViews] = useState(0);

  // Fetch video details
  useEffect(() => {
    axios.get(`http://localhost:8000/start/videos/${id}/videos`)
      .then(res => setVideo(res.data))
      .catch(err => console.error(err));
  }, [id]);

  // Fetch comments
  useEffect(() => {
    axios.get(`http://localhost:8000/start/videos/${id}/comments/`)
      .then(res => setComments(res.data))
      .catch(err => console.error(err));
  }, [id]);

  // Handle comment submission
  const handleCommentSubmit = async () => {
    const token = localStorage.getItem('accessToken');
    if (!token) {
      alert('You must be logged in to comment.');
      return;
    }

    try {
      const res = await axios.post(
        `http://localhost:8000/start/videos/${id}/comments/`,
        { text: commentText },
        {
          headers: {
            Authorization: `Token ${token}`,
            'Content-Type': 'application/json',
          },
        }
      );
      setComments(prev => [res.data, ...prev]);
      setCommentText('');
    } catch (err) {
      console.error(err);
      setError('Failed to post comment.');
    }
  };

  if (!video) return <div>Loading...</div>;

  return (
    <div className="p-4 max-w-2xl mx-auto">
      <ViewTracker 
        videoId={id} 
      />
      <video controls width="100%">
        <source src={`http://localhost:8000${video.file}`} type="video/mp4" />
      </video>
      <h2 className="text-2xl font-bold mt-4">{video.title}</h2>
      <p className="text-gray-600 mb-2">{video.description}</p>

      {/* Meta Info */}
      <div className="text-sm text-gray-500 mb-4">
        <span>{video.views || 0} views • </span>
        <span>{video.likes_count || 0} likes • </span>
        <span>{comments.length} comments</span>
      </div>

      {/* Comment Box */}
      <div className="mb-4">
        <textarea
          className="w-full p-2 border rounded"
          rows="2"
          value={commentText}
          onChange={e => setCommentText(e.target.value)}
          placeholder="Add a comment..."
        />
        <button
          onClick={handleCommentSubmit}
          className="bg-blue-500 text-white px-4 py-2 mt-2 rounded hover:bg-blue-600"
        >
          Submit Comment
        </button>
        {error && <p className="text-red-500 mt-2">{error}</p>}
      </div>

      {/* Display Comments */}
      <div>
        {comments.map((comment, i) => (
          <div key={i} className="border-t py-2">
            <p className="font-semibold">
              {comment.user?.username || 'Anonymous'}
            </p>
            <p>{comment.text}</p>
          </div>
        ))}
      </div>
    </div>
  );
};

export default VideoDetail;
