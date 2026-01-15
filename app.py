import tkinter as tk
from tkinter import messagebox

def simulate_reaction():
    selected_reaction = reaction_var.get()
    
    # Тазалау
    canvas.delete("all")
    
    # Пробирка салу
    canvas.create_rectangle(100, 50, 200, 250, outline="black", width=3)
    canvas.create_arc(100, 230, 200, 270, start=180, extent=180, outline="black", width=3)

    if selected_reaction == "Глюкоза + Cu(OH)2 (қыздыру)":
        # 1-кезең: Көк тұнба (Cu(OH)2)
        canvas.create_rectangle(103, 180, 197, 250, fill="blue", outline="")
        canvas.create_oval(103, 240, 197, 260, fill="blue", outline="")
        result_label.config(text="Нәтиже: Алдымен көк түсті Cu(OH)2 түзіледі.\nҚыздырғанда ол кірпіштей қызыл тұнбаға (Cu2O) айналады!", fg="red")
        # Тұнба түсін өзгерту (симуляция)
        root.after(2000, lambda: canvas.create_rectangle(103, 180, 197, 250, fill="#B22222", outline=""))
        root.after(2000, lambda: canvas.create_oval(103, 240, 197, 260, fill="#B22222", outline=""))

    elif selected_reaction == "Ақуыз (Биурет реакциясы)":
        # Күлгін түс
        canvas.create_rectangle(103, 180, 197, 250, fill="#8A2BE2", outline="")
        canvas.create_oval(103, 240, 197, 260, fill="#8A2BE2", outline="")
        result_label.config(text="Нәтиже: Ақуызға сілтілік ортада мыс купоросын қосқанда\nашық күлгін түс пайда болады.", fg="purple")

    elif selected_reaction == "Крахмал + Иод":
        # Көк-күлгін түс
        canvas.create_rectangle(103, 180, 197, 250, fill="#00008B", outline="")
        canvas.create_oval(103, 240, 197, 260, fill="#00008B", outline="")
        result_label.config(text="Нәтиже: Крахмал иодпен әрекеттесіп,\nкөк-күлгін түске боялады.", fg="blue")

# Негізгі терезе
root = tk.Tk()
root.title("Органикалық химия: Лабораториялық жұмыс")
root.geometry("400x500")

# Интерфейс элементтері
tk.Label(root, text="Реакцияны таңдаңыз:", font=("Arial", 12, "bold")).pack(pady=10)

reaction_var = tk.StringVar(value="Глюкоза + Cu(OH)2 (қыздыру)")
reactions = ["Глюкоза + Cu(OH)2 (қыздыру)", "Ақуыз (Биурет реакциясы)", "Крахмал + Иод"]
reaction_menu = tk.OptionMenu(root, reaction_var, *reactions)
reaction_menu.pack(pady=5)

btn_start = tk.Button(root, text="Тәжірибені бастау", command=simulate_reaction, bg="green", fg="white")
btn_start.pack(pady=10)

canvas = tk.Canvas(root, width=300, height=300)
canvas.pack()

result_label = tk.Label(root, text="", font=("Arial", 10, "italic"), wraplength=350)
result_label.pack(pady=10)

root.mainloop()
