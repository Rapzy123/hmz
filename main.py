import tkinter as tk
from tkinter import messagebox
import random
import webbrowser
import urllib.parse

whatsapp_number = "082143344242"
pesan = "iya aku mau."

def pindah_button(button):
    new_x = random.randint(0, window.winfo_width() - button.winfo_width())
    new_y = random.randint(0, window.winfo_height() - button.winfo_height())
    button.place(x=new_x, y=new_y)

def tekan_ya():
    messagebox.showinfo("Jawaban", "ak gbkl nyakitin km lg, aku gbs lupain km.")
    buka_whatsapp()

def tekan_tidak():
    pindah_button(tidak_button)

def buka_whatsapp():
    encoded_message = urllib.parse.quote(pesan)
    webbrowser.open_new(f"https://api.whatsapp.com/send?phone={6282143344242}&text={encoded_message}")

window = tk.Tk()
window.title("Aku Suka Kamu")
window.geometry("400x600")
window.configure(bg='#FFC0CB')  

frame = tk.Frame(window, bg='#FFC0CB', bd=5)
frame.place(relx=0.5, rely=0.5, anchor='center')

label = tk.Label(frame, text="km mw ga blikan sm ak?,\nksh ak 1 chance trkhir plis", font=("Helvetica", 16, "bold"), bg='#FFC0CB', fg='#FF69B4', justify=tk.CENTER)
label.pack(pady=20)

ya_button = tk.Button(frame, text="Yes", font=("Helvetica", 14), command=tekan_ya, bg='#FF69B4', fg='white', width=8)
ya_button.pack(side=tk.LEFT, padx=10)

tidak_button = tk.Button(window, text="No", font=("Helvetica", 14), command=tekan_tidak, bg='#FF69B4', fg='white', width=8)
tidak_button.place(x=50, y=50)

window.mainloop()