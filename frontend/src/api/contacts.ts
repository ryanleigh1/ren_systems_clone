import axios from "axios";
import { Contact } from "../types/contact";

const API_BASE = 'http://localhost:8000/api';


export const fetchContacts = async (): Promise<Contact[]> => {
  const response = await axios.get<Contact[]>(`${API_BASE}/contacts`);
  return response.data;
}