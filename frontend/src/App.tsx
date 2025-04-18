import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import ContactsPage from './pages/ContactsPage';
import HomePage from './pages/HomePage';

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<HomePage />} />
        <Route path="/contacts" element={<ContactsPage />} />
      </Routes>
    </Router>
  );
}

export default App;
