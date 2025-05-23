import { Input } from "./ui/input";
import { Search } from "lucide-react";
import { useContactsStore } from "@/store/contactsStore";

const SearchBar = () => {
  const {setIsSearching, setSearchQuery} = useContactsStore();
  const handleSearchChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    setSearchQuery(e.target.value); // Update the query in the store
  };

  return (
    <div className="relative w-full">
      <Search className="absolute left-3 top-1/2 -translate-y-1/2 text-muted-foreground h-5 w-5" />
      <Input
        type="search"
        placeholder="Search all contacts..."
        className="flex pl-10 w-full"
        onClick={() => setIsSearching(true)}
        onChange={handleSearchChange}
      />
    </div>
  )
};

export default SearchBar;