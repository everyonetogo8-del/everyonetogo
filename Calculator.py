import tkinter as tk




# -------------------------------
# Root window
# -------------------------------
root = tk.Tk()
root.title("Calculator")
root.geometry("350x250")
root.resizable(False, False)
root.configure(cursor="circle")





# -------------------------------
# Layout configuration
# -------------------------------
for i in range(4):
    root.grid_columnconfigure(i, weight=1)

# Entry fields
entry1 = tk.Entry(root, justify="center")
entry1.grid(row=0, column=0, columnspan=4, pady=5, sticky="ew")

entry2 = tk.Entry(root, justify="center")
entry2.grid(row=1, column=0, columnspan=4, pady=5, sticky="ew")

# Result display
result_label = tk.Label(root, text="Result will show here", anchor="center")
result_label.grid(row=2, column=0, columnspan=4, pady=5, sticky="ew")

# Styling
entry1.config(bg="#f0f0f0", font=("Calibri", 10, "bold"))
entry2.config(bg="#f0f0f0", font=("Calibri", 10, "bold"))
result_label.config(font=("Calibri", 10, "bold"), fg="green")



# -------------------------------
# Calculator functions
# -------------------------------
def add_numbers():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        result_label.config(text=str(num1 + num2))
    except ValueError:
        result_label.config(text="Invalid input!")


def subtract_numbers():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        result_label.config(text=str(num1 - num2))
    except ValueError:
        result_label.config(text="Invalid input!")


def multiply_numbers():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        result_label.config(text=str(num1 * num2))
    except ValueError:
        result_label.config(text="Invalid input!")


def divide_numbers():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        if num2 == 0:
            result_label.config(text="Cannot divide by zero!")
        else:
            result_label.config(text=str(num1 / num2))
    except ValueError:
        result_label.config(text="Invalid input!")


def on_enter(e):
    e.widget['background'] = "lightblue"




# -------------------------------
# Button customization settings
# -------------------------------
BUTTON_CONFIG = {
    "width": 3,
    "height": 1,
    "font": ("Arial", 10, "bold"),
    "bg": "#e0e0e0",
    "fg": "black",
    "hover_bg": "lightblue",
    "hover_fg": "black"
}




# -------------------------------
# Button creation with hover effects
# -------------------------------



def create_button(parent, text, command, row, column):
    btn = tk.Button(parent, text=text, command=command,
                    width=BUTTON_CONFIG["width"],
                    height=BUTTON_CONFIG["height"],
                    font=BUTTON_CONFIG["font"],
                    bg=BUTTON_CONFIG["bg"],
                    fg=BUTTON_CONFIG["fg"])
    btn.grid(row=row, column=column, padx=5, pady=5)

    # Hover effects
    def on_enter(e):
        e.widget['background'] = BUTTON_CONFIG["hover_bg"]
        e.widget['fg'] = BUTTON_CONFIG["hover_fg"]

    def on_leave(e):
        e.widget['background'] = BUTTON_CONFIG["bg"]
        e.widget['fg'] = BUTTON_CONFIG["fg"]

    btn.bind("<Enter>", on_enter)
    btn.bind("<Leave>", on_leave)
    return btn





# -------------------------------
# Buttons
# -------------------------------
buttons = [
    ("+", add_numbers),
    ("-", subtract_numbers),
    ("*", multiply_numbers),
    ("/", divide_numbers)
]

for idx, (symbol, func) in enumerate(buttons):
    create_button(root, symbol, func, row=3, column=idx)





# -------------------------------
# Run application
# -------------------------------
root.mainloop()
