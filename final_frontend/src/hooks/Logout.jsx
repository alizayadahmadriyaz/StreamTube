import { useNavigate } from 'react-router-dom';

const useLogout = () => {
  const navigate = useNavigate();

  const logout = () => {
    // Clear tokens or any user-related data from localStorage/sessionStorage
    localStorage.removeItem('accessToken');
    // Or clear all storage if needed: localStorage.clear();

    // Optionally clear any other app state or context here

    // Redirect to login or home page
    navigate('/'); // or navigate('/')
  };

  return logout;
};

export default useLogout;
