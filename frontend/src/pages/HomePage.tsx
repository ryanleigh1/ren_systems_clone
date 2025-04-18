import { useNavigate } from 'react-router-dom';

const HomePage = () => {
  const navigate = useNavigate();
  return (
    <div className="h-screen flex items-center justify-center">
      <button onClick={() => navigate('/contacts')}>Show Contacts</button>
    </div>
  );
}
export default HomePage;