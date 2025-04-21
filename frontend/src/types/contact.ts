export type Contact = {
  id: number;
  firstName: string;
  lastName: string;
  middleName?: string;
  dateOfBirth: Date;
  isVip?: boolean;
  emailAddresses?: { id: number; emailAddress: string; type: string }[]
  phoneNumbers?: { id: number; phone_number: string; type: string }[]
  webInfo?: { id: number; url: string; type: string }[]
}