import { create } from 'zustand';
import { fetchContacts } from '../api/contacts';
import { Contact } from '../types/contact';

type ContactStore = {
  contacts: Contact[],
  loading: boolean,
  error: string | null,
  setContacts: (contacts: Contact[]) => void,
  searchQuery: string,
  setSearchQuery: (query: string) => void,
  filteredContacts: () => Contact[],
  fetchContacts: () => Promise<void>,
}

export const useContactsStore = create<ContactStore>((set, get) => ({
  contacts: [],
  loading: false,
  error: null,
  setContacts: (contacts) => set({ contacts }),
  searchQuery: '',
  setSearchQuery: (query) => set({ searchQuery: query }),
  filteredContacts: () => {
    const { contacts, searchQuery } = get()
    if (!searchQuery.trim()) return contacts
    return contacts.filter((contact) =>
      `${contact.firstName} ${contact.lastName}`.toLowerCase().includes(searchQuery.toLowerCase())
    )
  },
  fetchContacts: async () => {
    set({ loading: true });
    try {
      const contacts = await fetchContacts();
      set({ contacts, loading: false });
    } catch (error: any) {
      set({ error: error.message, loading: false });
    }
  },
}))
