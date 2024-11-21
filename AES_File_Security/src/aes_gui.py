from tkinter import Tk, Label, Button, Entry, filedialog, messagebox
from src.aes_crypto import AESFileSecurity

class AESGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("AES File Security")
        self.root.geometry("400x300")
        
        # Key Input
        Label(root, text="Enter Key (max 16 chars):").pack(pady=10)
        self.key_entry = Entry(root, show="*", width=30)
        self.key_entry.pack()

        # Encrypt Button
        self.encrypt_btn = Button(root, text="Encrypt File", command=self.encrypt_file)
        self.encrypt_btn.pack(pady=10)

        # Decrypt Button
        self.decrypt_btn = Button(root, text="Decrypt File", command=self.decrypt_file)
        self.decrypt_btn.pack(pady=10)

        # Status Label
        self.status_label = Label(root, text="", fg="green")
        self.status_label.pack(pady=20)

    def get_key(self):
        key = self.key_entry.get()
        if not key or len(key) > 16:
            messagebox.showerror("Error", "Key must be 1-16 characters long.")
            return None
        return key.encode()

    def encrypt_file(self):
        key = self.get_key()
        if not key:
            return
        file_path = filedialog.askopenfilename(title="Select File to Encrypt")
        if not file_path:
            return
        output_file = filedialog.asksaveasfilename(title="Save Encrypted File As", defaultextension=".encrypted")
        if not output_file:
            return
        try:
            aes = AESFileSecurity(key)
            aes.encrypt(file_path, output_file)
            self.status_label.config(text="File encrypted successfully!", fg="green")
        except Exception as e:
            messagebox.showerror("Error", f"Encryption failed: {str(e)}")

    def decrypt_file(self):
        key = self.get_key()
        if not key:
            return
        file_path = filedialog.askopenfilename(title="Select File to Decrypt")
        if not file_path:
            return
        output_file = filedialog.asksaveasfilename(title="Save Decrypted File As")
        if not output_file:
            return
        try:
            aes = AESFileSecurity(key)
            aes.decrypt(file_path, output_file)
            self.status_label.config(text="File decrypted successfully!", fg="green")
        except Exception as e:
            messagebox.showerror("Error", f"Decryption failed: {str(e)}")

if __name__ == "__main__":
    root = Tk()
    gui = AESGUI(root)
    root.mainloop()
