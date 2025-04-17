import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import ContactsPage from './pages/ContactsPage';

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<ContactsPage />} />
        {/* You'll add a contact detail/edit page here later */}
      </Routes>
    </Router>
  );
}

export default App;
