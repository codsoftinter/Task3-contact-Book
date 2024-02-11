import tkinter as tk
from tkinter import messagebox

class AttractiveContactBook:
    def __init__(self, root):
        self.root = root
        self.root.title("Attractive Contact Book")

        # Contact list
        self.contacts = []

        # Styling
        root.geometry("600x400")
        root.configure(bg="#f0f0f0")

        # Title
        title_label = tk.Label(root, text="Contact Book", font=("Helvetica", 24, "bold"), bg="#f0f0f0", fg="#00897b")
        title_label.pack(pady=20)

        # Entry fields
        self.name_entry = self.create_entry("Name")
        self.phone_entry = self.create_entry("Phone")
        self.email_entry = self.create_entry("Email")
        self.address_entry = self.create_entry("Address")

        # Buttons
        self.create_button("Add Contact", self.add_contact, bg="#4caf50", fg="white")
        self.create_button("View Contacts", self.view_contacts, bg="#2196f3", fg="white")
        self.create_button("Search Contact", self.search_contact, bg="#ff9800", fg="white")
        self.create_button("Update Contact", self.update_contact, bg="#795548", fg="white")
        self.create_button("Delete Contact", self.delete_contact, bg="#f44336", fg="white")

    def create_entry(self, placeholder):
        entry = tk.Entry(self.root, font=("Arial", 14), borderwidth=2)
        entry.insert(0, placeholder)
        entry.bind("<FocusIn>", lambda event: entry.delete(0, tk.END))
        entry.bind("<FocusOut>", lambda event: entry.insert(0, placeholder) if not entry.get() else None)
        entry.pack(pady=10)
        return entry

    def create_button(self, text, command, bg, fg):
        button = tk.Button(self.root, text=text, command=command, font=("Helvetica", 14, "bold"), bg=bg, fg=fg)
        button.pack(pady=10)
        return button

    def add_contact(self):
        name = self.name_entry.get()
        phone = self.phone_entry.get()
        email = self.email_entry.get()
        address = self.address_entry.get()

        if name and phone:
            contact = {"Name": name, "Phone": phone, "Email": email, "Address": address}
            self.contacts.append(contact)
            messagebox.showinfo("Success", "Contact added successfully!")
            self.clear_entries()
        else:
            messagebox.showwarning("Incomplete Information", "Please enter at least Name and Phone.")

    def view_contacts(self):
        if not self.contacts:
            messagebox.showinfo("Empty", "No contacts available.")
        else:
            contacts_info = ""
            for idx, contact in enumerate(self.contacts, start=1):
                contacts_info += f"{idx}. Name: {contact['Name']}, Phone: {contact['Phone']}\n"
            messagebox.showinfo("Contacts", contacts_info)

    def search_contact(self):
        search_term = self.name_entry.get().lower()
        if not search_term:
            messagebox.showwarning("Search", "Please enter a name for search.")
            return

        matching_contacts = [contact for contact in self.contacts if search_term in contact["Name"].lower()]
        if not matching_contacts:
            messagebox.showinfo("Search Result", "No matching contacts found.")
        else:
            contacts_info = ""
            for idx, contact in enumerate(matching_contacts, start=1):
                contacts_info += f"{idx}. Name: {contact['Name']}, Phone: {contact['Phone']}\n"
            messagebox.showinfo("Search Result", contacts_info)

    def update_contact(self):
        index = self.get_selected_index()
        if index is not None:
            name = self.name_entry.get()
            phone = self.phone_entry.get()
            email = self.email_entry.get()
            address = self.address_entry.get()

            if name and phone:
                self.contacts[index] = {"Name": name, "Phone": phone, "Email": email, "Address": address}
                messagebox.showinfo("Success", "Contact updated successfully!")
                self.clear_entries()
            else:
                messagebox.showwarning("Incomplete Information", "Please enter at least Name and Phone.")
        else:
            messagebox.showwarning("No Selection", "Please select a contact to update.")

    def delete_contact(self):
        index = self.get_selected_index()
        if index is not None:
            confirmed = messagebox.askyesno("Confirm Deletion", "Are you sure you want to delete this contact?")
            if confirmed:
                del self.contacts[index]
                messagebox.showinfo("Success", "Contact deleted successfully!")
                self.clear_entries()
        else:
            messagebox.showwarning("No Selection", "Please select a contact to delete.")

    def get_selected_index(self):
        try:
            selected_index = int(messagebox.askstring("Select Contact", "Enter the contact number:")) - 1
            if 0 <= selected_index < len(self.contacts):
                return selected_index
            else:
                messagebox.showwarning("Invalid Selection", "Please enter a valid contact number.")
        except ValueError:
            messagebox.showwarning("Invalid Input", "Please enter a valid number.")
        return None

    def clear_entries(self):
        self.name_entry.delete(0, tk.END)
        self.phone_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)
        self.address_entry.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = AttractiveContactBook(root)
    root.mainloop()
