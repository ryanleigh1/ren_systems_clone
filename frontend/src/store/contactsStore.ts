import { create } from 'zustand';
import { fetchContacts } from '../api/contacts';
import { Contact } from '../types/contact';

interface ContactStore {
  // State
  contacts: Contact[];
  loading: boolean;
  error: string | null;
  isSidePanelOpen: boolean;
  searchQuery: string;
  selectedContact: Contact | null;
  filteredContacts: () => Contact[];
  // Actions
  fetchContacts: () => Promise<void>;
  setContacts: (contacts: Contact[]) => void,
  setSearchQuery: (query: string) => void,
  setSelectedContact: (contact: Contact | null) => void,
  setSidePanelOpen: (isOpen: boolean) => void,
}

export const useContactsStore = create<ContactStore>((set, get) => ({
  // default state
  contacts: [],
  loading: false,
  error: null,
  isSidePanelOpen: false,
  searchQuery: '',
  selectedContact: null,
  filteredContacts: () => {
    const { contacts, searchQuery } = get()
    if (!searchQuery.trim()) return contacts
    return contacts.filter((contact) =>
      `${contact.firstName} ${contact.lastName}`.toLowerCase().includes(searchQuery.toLowerCase())
    )
  },
  // Actions
  fetchContacts: async () => {
    set({ loading: true });
    try {
      const contacts = await fetchContacts();
      set({ contacts, loading: false });
    } catch (error: any) {
      set({ error: error.message, loading: false });
    }
  },
  setContacts: (contacts) => set({ contacts }),
  setSelectedContact: (contact) => set({ selectedContact: contact }),
  setSearchQuery: (query) => set({ searchQuery: query }),
  setSidePanelOpen: (isOpen) => set({ isSidePanelOpen: isOpen}),
}))
