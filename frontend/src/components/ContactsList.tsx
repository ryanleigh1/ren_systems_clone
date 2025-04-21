import { useEffect } from "react";
import { useContactsStore } from "../store/contactsStore";
import { Contact } from "../types/contact";

const ContactsList = () => {
  const { contacts, loading, error, fetchContacts, setSelectedContact, setSidePanelOpen } = useContactsStore();

  useEffect(() => {
    fetchContacts();
  }, [fetchContacts]);

  if (loading) return <p>Loading contacts...</p>;
  if (error) return <p>Error: {error}</p>;

  const setSelectedContactAndOpenPanel = (contact: Contact) => {
    setSelectedContact(contact);
    setSidePanelOpen(true);
  };

  return (
    <div className="h-screen w-full flex justify-center align-middle bg-gray-100 p-4">
      <ul>
        {contacts.map((contact) => {
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