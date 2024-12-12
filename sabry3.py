import tkinter as tk
from tkinter import messagebox
from gtts import gTTS
import os

def play_text():
    text = text_entry.get().strip()
    if text:
        try:
            tts = gTTS(text, lang='en')
            tts.save("output.mp3")
            os.system("start output.mp3" if os.name == "nt" else "open output.mp3")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")
    else:
        messagebox.showwarning("Warning", "Please enter some text to play.")

def exit_app():
    root.destroy()

def dummy_set_function():
    messagebox.showinfo("Set Button", "This button is a placeholder.")

root = tk.Tk()
root.title("Voice Generator")
root.geometry("400x300")
root.configure(bg="black")

label = tk.Label(root, text="Convert Text to Voice", font=("Arial", 16, "bold"), bg="black", fg="white")
label.pack(pady=10)


text_entry = tk.Entry(root, font=("Arial", 14), width=30, bg="black", fg="white", insertbackground="white")
text_entry.pack(pady=10)

button_frame = tk.Frame(root, bg="black")
button_frame.pack(pady=20)

play_button = tk.Button(button_frame, text="Play", command=play_text, font=("Arial", 12), bg="darkorange", fg="white", width=8)
play_button.grid(row=0, column=0, padx=10)

set_button = tk.Button(button_frame, text="Set", command=dummy_set_function, font=("Arial", 12), bg="darkblue", fg="white", width=8)
set_button.grid(row=0, column=1, padx=10)

exit_button = tk.Button(button_frame, text="Exit", command=exit_app, font=("Arial", 12), bg="crimson", fg="white", width=8)
exit_button.grid(row=0, column=2, padx=10)

footer_label = tk.Label(root, text="Developed by :Ahmed Sabry Abdel Salam", font=("Arial", 10, "italic"), bg="black", fg="gray")
footer_label.pack(side="bottom", pady=5)

root.mainloop()