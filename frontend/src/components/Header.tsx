import SearchBar from "./SearchBar";

const Header = () => {
  return (
    <header className="flex justify-center items-center sticky top-0 z-10 h-16 py-4 w-full bg-white shadow-md">
      <div className=" w-full max-w-4xl">
        <SearchBar />
      </div>
    </header>
  );
};

export default Header;
