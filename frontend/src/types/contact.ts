export type Contact = {
  id: number;
  firstName: string;
  lastName: string;
  middleName?: string;
  dateOfBirth: Date;
  isVip?: boolean;
}