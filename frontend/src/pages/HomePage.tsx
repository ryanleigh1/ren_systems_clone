import ContactsList from "../components/ContactsList";
import SearchBar from "../components/SearchBar";
import ContactsSidePanel from "../components/ContactsSidePanel";

const HomePage = () => {
  return (
    <div className="h-screen flex items-center justify-center">
      <div className="search-bar-container">
        <SearchBar />
      </div>
      
      <div className="contacts-list-container">
        <ContactsList />
      </div>

      <div className="contacts-side=panel-container">
        <ContactsSidePanel />
      </div>
    </div>
  );
}
export default HomePage;