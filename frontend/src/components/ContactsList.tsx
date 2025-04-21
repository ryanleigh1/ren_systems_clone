import { useContactsStore } from "../store/contactsStore";
import { Contact } from "../types/contact";

const ContactsList = () => {
  const { loading, error, filteredContacts, setSelectedContact, setSidePanelOpen } = useContactsStore();


  if (loading) return <p>Loading contacts...</p>;
  if (error) return <p>Error: {error}</p>;

  const setSelectedContactAndOpenPanel = (contact: Contact) => {
    setSelectedContact(contact);
    setSidePanelOpen(true);
  };

  return (
    <div className="h-screen w-full flex justify-center align-middle bg-gray-100 mt-20 p-4">
      <ul>
        {filteredContacts.map((contact) => {
          return (
            <li key={contact.id}>
              <button onClick={() => setSelectedContactAndOpenPanel(contact)}>{contact.firstName}</button>
            </li>
          )
        })}
      </ul>
    </div>
  )
}

export default ContactsList;