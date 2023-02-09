import tkinter as tk
from tkinter import filedialog
import os

root = tk.Tk()
root.geometry("400x100")
root.config(bg="#363636")
root.title("Reproductor Multimedia")


def play_music():
    file_path = filedialog.askopenfilename()
    os.system("start " + file_path)

play_button = tk.Button(root, text="Buscar Archivo para reproducir", command=play_music, bg="#222222", fg="white", font=("Helvetica", 16))
play_button.pack(pady=20)

root.mainloop()
