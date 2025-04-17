import { useEffect, useState } from "react";
import { Contact } from "../types/contact";
import { fetchContacts } from "../api/contacts";

const ContactsList = () => {
  const [contacts, setContacts] = useState<Contact[]>([]);

  useEffect(() => {
    fetchContacts().then(setContacts);
  }, []);

  return (
    <div>
      <ul>
        {contacts.map((contact) => {
          console.log('contact', contact)
          return (
            <li key={contact.id}>{contact.firstName}</li>
          )
        })}
      </ul>
    </div>
  )
}

export default ContactsList;