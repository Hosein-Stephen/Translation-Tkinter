from googletrans import Translator, LANGUAGES
import customtkinter as ctk
from tkinter import messagebox
import webbrowser
from tkinter import *

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

root = ctk.CTk()
root.geometry("1000x500")
root.title("Hosein Stephen")
root.resizable(0,0)

srclang = ctk.StringVar()
tgtlang = ctk.StringVar()

frame = ctk.CTkFrame(root)
frame.pack(pady=12,padx=12,expand=True,fill="both")

label = ctk.CTkLabel(frame, text="Welcome to Stephen translator.",font=("Segoe UI", 16, "bold"))
label.place(relx=0.5,rely=0.05, anchor="center")

input = ctk.CTkTextbox(frame,width=350, height=350)
input.place(rely=0.5,relx=0.2,anchor="center")

output = ctk.CTkTextbox(frame, width=350, height=350)
output.place(rely=0.5,relx=0.8,anchor="center")

language = list(LANGUAGES.values())





endlang = ctk.CTkComboBox(frame,width=200,values=language,)
endlang.place(relx=0.7,rely=0.05)
endlang.set("Choose output language")

srclang = ctk.CTkComboBox(frame, variable=srclang, values=language,width=200)
srclang.place(relx=0.1,rely=0.05)
srclang.set("Choose Input language")

def Translate():
    transaltor = Translator()
    translated = transaltor.translate(text=input.get(1.0, ctk.END), src=srclang.get(), dest=endlang.get())
    output.delete(1.0, ctk.END)
    output.insert(ctk.END, translated.text)
    with open("Hosein_Translator.txt", "a", encoding="utf-8") as file:
            file.write(f"{translated.text}: {input.get(1.0, ctk.END)}\n")


startbutton = ctk.CTkButton(frame,text="Translate",height=50,width=150, command=Translate)
startbutton.place(relx=0.5, rely=0.5, anchor="center")



root.mainloop()
