import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import HomePage from './pages/HomePage';
import { useEffect } from 'react';
import { useContactsStore } from './store/contactsStore';

function App() {
  const fetchContacts = useContactsStore((state) => state.fetchContacts);
  useEffect(() => {
    fetchContacts();
  }, [fetchContacts]);
  
  return (
    <Router>
      <Routes>
        <Route path="/" element={<HomePage />} />
      </Routes>
    </Router>
  );
}

export default App;
