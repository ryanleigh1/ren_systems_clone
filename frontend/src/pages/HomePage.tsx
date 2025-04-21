import ContactsList from "@/components/ContactsList";
import ContactsSidePanel from "@/components/ContactsSidePanel";
import Header from "@/components/Header";

const HomePage = () => {
  return (
    <div className="h-screen w-screen flex flex-col items-center justify-center gap-4 m-4">
      <div className="w-full max-w-4xl flex flex-col gap-4">
        <Header />

        <div className="contacts-list-container ">
          <ContactsList />
        </div>

        <div className="contacts-side=panel-container">
          <ContactsSidePanel />
        </div>
      </div>
    </div>
  );
};
export default HomePage;
