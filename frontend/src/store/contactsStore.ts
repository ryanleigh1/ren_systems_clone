import { create } from "zustand";
import { fetchContacts } from "../api/contacts";
import { Contact } from "../types/contact";

interface ContactState {
  // State
  contacts: Contact[];
  loading: boolean;
  error: string | null;
  isSearching: boolean;
  isSidePanelOpen: boolean;
  searchQuery: string;
  selectedContact: Contact | null;
  
  filteredContacts: Contact[];
}

interface Actions {
  fetchContacts: () => Promise<void>;
  setContacts: (contacts: Contact[]) => void;
  setIsSearching: (isSearching: boolean) => void;
  setSearchQuery: (query: string) => void;
  setSelectedContact: (contact: Contact | null) => void;
  setSidePanelOpen: (isOpen: boolean) => void;
}

export const useContactsStore = create<ContactState & Actions>((set, get) => ({
  // default state
  contacts: [],
  loading: false,
  error: null,
  isSearching: false,
  isSidePanelOpen: false,
  searchQuery: "",
  selectedContact: null,
  filteredContacts: [],
  
  // Actions
  fetchContacts: async () => {
    set({ loading: true });
    try {
      const contacts = await fetchContacts();
      set({ contacts, filteredContacts: contacts, loading: false });
    } catch (error: any) {
      set({ error: error.message, loading: false });
    }
  },
  setContacts: (contacts) => set({ contacts }),
  setIsSearching: (isSearching) => set({ isSearching }),
  setSelectedContact: (contact) => set({ selectedContact: contact }),
  setSidePanelOpen: (isOpen) => set({ isSidePanelOpen: isOpen }),
  setSearchQuery: (query: string) => {
    set({ searchQuery: query });
    const { contacts } = get();
    if (!query.trim()) {
      set({ filteredContacts: contacts });
    } else {
      const filtered = contacts.filter(
        (contact) =>
          contact.firstName.toLowerCase().includes(query.toLowerCase()) ||
          contact.lastName.toLowerCase().includes(query.toLowerCase())
      );
      set({ filteredContacts: filtered });
    }
  },
}));
