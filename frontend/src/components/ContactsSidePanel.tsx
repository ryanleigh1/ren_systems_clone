import { useContactsStore } from "../store/contactsStore";
import { motion, AnimatePresence } from "framer-motion";
import {
  ArrowRightToLine,
  BellOff,
  CircleUser,
  Mail,
  Pencil,
  Phone,
} from "lucide-react";

const ContactsSidePanel = () => {
  const { selectedContact, isSidePanelOpen, setSidePanelOpen } =
    useContactsStore();

  const closeSidePanel = () => {
    setSidePanelOpen(false);
  };

  const renderEmails = () => {
    if (!selectedContact?.emailAddresses) return null;
    return (
      <ul className="flex flex-col gap-y-2 mb-2">
        {selectedContact.emailAddresses.map((emailDetails, index) => (
          <li key={index} className="flex gap-x-4">
            <Mail />
            <span className="flex flex-col gap-x-2">
              <p>{emailDetails.type}</p>
              <p>{emailDetails.emailAddress}</p>
            </span>
          </li>
        ))}
      </ul>
    );
  };

  const renderPhoneNumbers = () => {
    if (!selectedContact?.phoneNumbers) return null;
    return (
      <ul className="flex flex-col gap-y-2">
        {selectedContact.phoneNumbers.map((phoneDetails, index) => (
          <li key={index} className="flex gap-x-4">
            <Phone />
            <span className="flex flex-col gap-x-2">
              <p>{phoneDetails.type}</p>
              <p>{phoneDetails.phone_number}</p>
            </span>
          </li>
        ))}
      </ul>
    );
  };

  return (
    <AnimatePresence>
      {selectedContact && isSidePanelOpen && (
        <motion.div
          key="sidepanel"
          initial={{ x: "100%" }}
          animate={{ x: 0 }}
          exit={{ x: "100%" }}
          transition={{ type: "tween", duration: 0.3 }}
          className="fixed top-0 right-0 flex flex-col gap-y-6 h-full w-full sm:w-[400px] bg-white shadow-lg z-50 p-4"
        >
          <div className="flex justify-start gap-x-4">
            <button
              onClick={() => closeSidePanel()}
              className="mt-4 text-sm text-blue-500 hover:underline"
            >
              <ArrowRightToLine />
            </button>
            <button
              onClick={() => console.log("Edit contact")}
              className="mt-4 text-sm text-blue-500 hover:underline"
            >
              <Pencil />
            </button>
          </div>
          {/* TODO: move this into separate component */}
          <div className="contact-info flex align-middle justify-between">
            <CircleUser size={32} />
            <span>
              <button>
                <BellOff />
              </button>
              <button></button>
            </span>
          </div>

          <div className="contact-name-container">
            <p>
              {selectedContact.firstName} {selectedContact.lastName}
            </p>
          </div>

          {/* contact methods */}
          <div>
            <div className="border-b-1 border-gray-300 mb-4">
              <p className="text-gray-400 tracking-wide py-2">Contact</p>
            </div>
            {renderEmails()}
            {renderPhoneNumbers()}
          </div>
        </motion.div>
      )}
    </AnimatePresence>
  );
};

export default ContactsSidePanel;
