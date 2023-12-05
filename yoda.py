import tkinter as tk

def send():
    name = name_entry.get()
    message = entry.get()
    full_message = name + ": " + message

    response = "Merhaba " + name + "! Nasıl yardımcı olabilirim?"

    chatlog.config(state=tk.NORMAL)
    chatlog.insert(tk.END, full_message + "\n")
    chatlog.insert(tk.END, "Pyrexyoda: " + response + "\n")
    chatlog.config(state=tk.DISABLED)

    entry.delete(0, tk.END)

def set_name():
    name = name_entry.get()

    if name:
        name_label.grid_forget()
        name_entry.grid_forget()
        set_name_button.grid_forget()
        entry.config(state=tk.NORMAL)
        entry.focus()

window = tk.Tk()
window.title("pyrex chatbot")

name_label = tk.Label(window, text="Lütfen adınızı girin:")
name_label.grid(row=0, column=0, padx=10, pady=10)
name_entry = tk.Entry(window, width=50)
name_entry.grid(row=0, column=1, padx=10, pady=10)


set_name_button = tk.Button(window, text="Adımı Kaydet", command=set_name)
set_name_button.grid(row=0, column=2, padx=10, pady=10)

chatlog = tk.Text(window, bg="white", height=20, width=50)
chatlog.config(state=tk.DISABLED)
chatlog.grid(row=1, column=0, padx=10, pady=10)


photo = tk.PhotoImage(file="resim.png")
image_label = tk.Label(window, image=photo)
image_label.grid(row=1, column=1, padx=10, pady=10)


entry = tk.Entry(window, width=50, state=tk.DISABLED)
entry.bind("<Return>", lambda x: send())
entry.grid(row=2, column=0, padx=10, pady=10)

window.mainloop()
