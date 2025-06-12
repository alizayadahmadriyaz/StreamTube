import React, { useState,useEffect } from 'react';
import axios from 'axios';

const SubscriptionButton = ({ creatorId, isSubscribedInitial = false }) => {
  const [isSubscribed, setIsSubscribed] = useState(false);
  const [loading, setLoading] = useState(false);
  const [hua, sethua] = useState(false);

  // Optionally, fetch initial subscription status from API
  // useEffect(() => { ... }, [creatorId]);

  const token = localStorage.getItem('accessToken');
  console.log('asli nakli')
  // console.log('eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzQ5NTgwNTQ1LCJpYXQiOjE3NDk1NzY5NDUsImp0aSI6ImU2MjhkZTQxMTZkYTQxNzBiZjJmYTI2ZjI4ZTFlZjEyIiwidXNlcl9pZCI6OH0.YhxLhjuCow8OX-G1I_w8hcEgcK2FwB9qJzARDIUBKFY')
  console.log(token);
  useEffect(() => {
    const token = localStorage.getItem('accessToken');
    if (!token) {
      console.error("No access token found");
      return;
    }
  
    axios.get(`http://localhost:8000/start/users/${creatorId}/subscribe/`, {
      headers: { Authorization: `Bearer ${token}` }
    })
    .then(res => sethua(res.data))
    .catch(err => console.error(err));
  }, [creatorId]);
  
  console.log('result')
  console.log(hua)

  const handleSubscribe = async () => {
    setLoading(true);
    try {
      await axios.post(
        `http://localhost:8000/start/users/${creatorId}/subscribe/`,
        { creator: creatorId },
        {
          headers: {
            Authorization: `Bearer ${token}`,
            'Content-Type': 'application/json',
          },
        }
      );
      setIsSubscribed(true);
    } catch (err) {
      alert('Failed to subscribe.');
    } finally {
      setLoading(false);
    }
  };

  const handleUnsubscribe = async () => {
    setLoading(true);
    try {
      await axios.delete(
        `http://localhost:8000/start/users/${creatorId}/subscribe/`,
        {
          headers: {
            Authorization: `Bearer ${token}`,
          },
        }
      );
      setIsSubscribed(false);
    } catch (err) {
      alert('Failed to unsubscribe.');
    } finally {
      setLoading(false);
    }
  };
  const mess=hua?.message;
  console.log(mess)
  console.log((isSubscribed || (mess)))
  return (
    <button
      onClick={isSubscribed ? handleUnsubscribe : handleSubscribe}
      disabled={loading}
      className={`px-6 py-2 rounded-lg font-semibold transition ${
        (isSubscribed || (mess))
          ? 'bg-gray-300 text-gray-700 hover:bg-gray-400'
          : 'bg-red-500 text-white hover:bg-red-600'
      }`}
    >
      {loading
        ? 'Processing...'
        : (isSubscribed || (mess))
        ? 'Subscribed'
        : 'Subscribe'}
    </button>
  );
};

export default SubscriptionButton;
