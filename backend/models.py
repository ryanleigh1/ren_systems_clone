from sqlalchemy import Column, Integer, String, Date, Boolean, ForeignKey, Enum as SQLEnum
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

from enum import Enum

Base = declarative_base()

class PhoneType(Enum):
    home = "home"
    work = "work"
    mobile = "mobile"

class EmailType(Enum):
    personal = "personal"
    work = "work"
    
class WebInfoType(Enum):
    personal = "personal"
    work = "work"
    linkedin = "linkedin"


class Contact(Base):
    __tablename__ = 'contacts'  # Name of the table in the database

    id = Column(Integer, primary_key=True, autoincrement=True)  # Primary key
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    middle_name = Column(String, nullable=False)
    date_of_birth = Column(Date, nullable=True)
    is_vip = Column(Boolean, default=False)
    
    email_addresses = relationship("ContactEmails", back_populates="contact", cascade="all, delete-orphan")
    phone_numbers = relationship("ContactPhoneNumbers", back_populates="contact", cascade="all, delete-orphan")
    web_info = relationship("ContactWebInfo", back_populates="contact", cascade="all, delete-orphan")
    
    def __repr__(self):
        return f"<Contact(name={self.first_name}, email={self.email})>"
      
class ContactEmails(Base):
    __tablename__ = 'contact_email_addresses'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    contact_id = Column(Integer, ForeignKey('contacts.id'), nullable=False)
    email_address = Column(String, nullable=False)
    type = Column(SQLEnum(EmailType, name="email_type"), nullable=False, default=EmailType.personal)  # Enum for email type
    
    contact = relationship("Contact", back_populates="email_addresses")
    
    def __repr__(self):
        return f"<CustomerEmails(email={self.email})>"
      
class ContactPhoneNumbers(Base):
    __tablename__ = 'contact_phone_numbers'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    contact_id = Column(Integer, ForeignKey('contacts.id'), nullable=False)
    phone_number = Column(String, nullable=False)
    type = Column(SQLEnum(PhoneType, name="phone_type"), nullable=False, default=PhoneType.mobile)  # Enum for phone type
    
    contact = relationship("Contact", back_populates="phone_numbers")
    
    def __repr__(self):
        return f"<ContactPhoneNumbers(phone={self.phone_number})>"
      
class ContactWebInfo(Base):
    __tablename__ = 'contact_web_info'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    contact_id = Column(Integer, ForeignKey('contacts.id'), nullable=False)
    url = Column(String, nullable=False)
    type = Column(SQLEnum(WebInfoType, name="web_info_type"), nullable=False, default=WebInfoType.personal)  # Enum for web info type
    
    contact = relationship("Contact", back_populates="web_info")
    
    def __repr__(self):
        return f"<ContactWebInfo(url={self.url})>"