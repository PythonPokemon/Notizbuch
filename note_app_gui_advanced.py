import tkinter as tk
from tkinter import messagebox, ttk
import json

class NoteAppGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Notizbuch")

        self.notes = {}

        self.load_notes()

        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(fill="both", expand=True)

        self.add_note_tab()
        self.view_notes_tab()

    def add_note_tab(self):
        add_tab = ttk.Frame(self.notebook)
        self.notebook.add(add_tab, text="Notiz hinzufügen")

        title_label = tk.Label(add_tab, text="Titel:")
        title_label.pack(padx=10, pady=5)

        self.title_entry = tk.Entry(add_tab)
        self.title_entry.pack(padx=10, pady=5)

        content_label = tk.Label(add_tab, text="Inhalt:")
        content_label.pack(padx=10, pady=5)

        self.content_text = tk.Text(add_tab, height=10, width=40)
        self.content_text.pack(padx=10, pady=5)

        add_button = tk.Button(add_tab, text="Notiz hinzufügen", command=self.add_note)
        add_button.pack(padx=10, pady=5)

    def view_notes_tab(self):
        view_tab = ttk.Frame(self.notebook)
        self.notebook.add(view_tab, text="Notizen anzeigen")

        self.note_listbox = tk.Listbox(view_tab)
        self.note_listbox.pack(padx=10, pady=5, fill="both", expand=True)

        view_button = tk.Button(view_tab, text="Notiz anzeigen", command=self.view_note)
        view_button.pack(padx=10, pady=5)

        self.note_content_text = tk.Text(view_tab, height=10, width=40)
        self.note_content_text.pack(padx=10, pady=5)

        self.update_note_listbox()

    def add_note(self):
        title = self.title_entry.get()
        content = self.content_text.get("1.0", "end-1c")
        self.notes[title] = content
        messagebox.showinfo("Erfolg", "Notiz hinzugefügt.")
        self.title_entry.delete(0, "end")
        self.content_text.delete("1.0", "end")
        self.update_note_listbox()

    def view_note(self):
        selected_note = self.note_listbox.get(tk.ACTIVE)
        if selected_note:
            self.note_content_text.delete("1.0", "end")
            self.note_content_text.insert("1.0", self.notes[selected_note])

    def update_note_listbox(self):
        self.note_listbox.delete(0, tk.END)
        for note in self.notes:
            self.note_listbox.insert(tk.END, note)

    def load_notes(self):
        try:
            with open("notes.json", "r") as file:
                self.notes = json.load(file)
        except FileNotFoundError:
            self.notes = {}

    def save_notes(self):
        with open("notes.json", "w") as file:
            json.dump(self.notes, file)
        messagebox.showinfo("Erfolg", "Notizen gespeichert.")

if __name__ == "__main__":
    root = tk.Tk()
    app = NoteAppGUI(root)
    root.protocol("WM_DELETE_WINDOW", app.save_notes)
    root.mainloop()
