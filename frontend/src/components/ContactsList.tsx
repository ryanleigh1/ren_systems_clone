import { useEffect } from "react";
import { useContactsStore } from "../store/contactsStore";

const ContactsList = () => {
  const { contacts, loading, error, fetchContacts } = useContactsStore();

  useEffect(() => {
    fetchContacts();
  }, [fetchContacts]);

  if (loading) return <p>Loading contacts...</p>;
  if (error) return <p>Error: {error}</p>;

  return (
    <div className="h-screen w-full flex justify-center align-middle bg-gray-100 p-4">
      <ul>
        {contacts.map((contact) => {
          return (
            <li key={contact.id}>{contact.firstName}</li>
          )
        })}
      </ul>
    </div>
  )
}

export default ContactsList;