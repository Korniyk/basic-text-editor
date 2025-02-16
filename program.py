import tkinter as tk
from tkinter import filedialog


class TextEditorModel:
    def __init__(self):
        self.content = ""

    def load_content(self, file_path):
        with open(file_path, "r", encoding="utf-8") as file:
            self.content = file.read()
        return self.content

    def save_content(self, file_path, content):
        with open(file_path, "w", encoding="utf-8") as file:
            file.write(content)

    def clear_content(self):
        self.content = ""


class TextEditorController:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def open_file(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            content = self.model.load_content(file_path)
            self.view.update_text_area(content)

    def save_file(self):
        file_path = filedialog.asksaveasfilename(
            defaultextension=".txt",
            filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")],
        )
        if file_path:
            self.model.save_content(file_path, self.view.get_text_area_content())

    def clear_text(self):
        self.model.clear_content()
        self.view.update_text_area("")


class TextEditorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Текстовий редактор")
        self.root.geometry("800x600")
        self.root.configure(bg="#f0f0f0")

        self.model = TextEditorModel()
        self.controller = TextEditorController(self.model, self)
        self.create_widgets()

    def create_widgets(self):
        self.text_area = tk.Text(
            self.root,
            wrap="word",
            font=("Arial", 14),
            bg="#ffffff",
            fg="#000000",
            padx=10,
            pady=10,
        )
        self.text_area.pack(expand=True, fill="both")

        self.menu = tk.Menu(self.root)
        self.root.config(menu=self.menu)

        file_menu = tk.Menu(self.menu, tearoff=False)
        file_menu.add_command(label="Відкрити", command=self.controller.open_file)
        file_menu.add_command(label="Зберегти", command=self.controller.save_file)
        file_menu.add_separator()
        file_menu.add_command(label="Вийти", command=self.root.quit)

        self.menu.add_cascade(label="Файл", menu=file_menu)

        edit_menu = tk.Menu(self.menu, tearoff=False)
        edit_menu.add_command(label="Очистити", command=self.controller.clear_text)

        self.menu.add_cascade(label="Редагування", menu=edit_menu)

    def update_text_area(self, content):
        self.text_area.delete(1.0, tk.END)
        self.text_area.insert(tk.END, content)

    def get_text_area_content(self):
        return self.text_area.get(1.0, tk.END)


if __name__ == "__main__":
    root = tk.Tk()
    app = TextEditorApp(root)
    root.mainloop()
