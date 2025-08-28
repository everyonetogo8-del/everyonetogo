import tkinter as tk


#Root window
root = tk.Tk()
root.title("Calculator")
root.geometry("300x200")
root.resizable(False, False)
root.configure(cursor="circle")



# Layout
for i in range(4):
    root.grid_columnconfigure(i, weight=1)

entry1 = tk.Entry(root, justify="center")
entry1.grid(row=0, column=0, columnspan=4, pady=5, sticky="ew")

entry2 = tk.Entry(root, justify="center")
entry2.grid(row=1, column=0, columnspan=4, pady=5, sticky="ew")

result_label = tk.Label(root, text="Result will show here", anchor="center")
result_label.grid(row=2, column=0, columnspan=4, pady=5, sticky="ew")

entry1.config(bg="#f0f0f0", font=("Arial", 10, "bold"))
entry2.config(bg="#f0f0f0", font=("Arial", 10, "bold"))
result_label.config(font=("Calibri", 10, "bold"), fg="green")






# Functions
def add_numbers():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        result = num1 + num2
        result_label.config(text=str(result))
    except ValueError:
        result_label.config(text="Invalid input!")


def subtract_numbers():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        result = num1 - num2
        result_label.config(text=str(result))
    except ValueError:
        result_label.config(text="Invalid input!")


def multiply_numbers():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        result = num1 * num2
        result_label.config(text=str(result))
    except ValueError:
        result_label.config(text="Invalid input!")


def divide_numbers():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        if num2 == 0:
            result_label.config(text="Cannot divide by zero!")
        else:
            result = num1 / num2
            result_label.config(text=str(result))
    except ValueError:
        result_label.config(text="Invalid input!")


def on_enter(e):
    e.widget['background'] = "lightblue"


def on_leave(e):
    e.widget['background'] = "SystemButtonFace"





# Buttons
add_button = tk.Button(root, text="+", command=add_numbers, width=5)
add_button.grid(row=3, column=0, padx=2, pady=2)

sub_button = tk.Button(root, text="-", command=subtract_numbers, width=5)
sub_button.grid(row=3, column=1, padx=2, pady=2)

multiply_button = tk.Button(root, text="*", command=multiply_numbers, width=5)
multiply_button.grid(row=3, column=2, padx=2, pady=2)

divide_button = tk.Button(root, text="/", command=divide_numbers, width=5)
divide_button.grid(row=3, column=3, padx=2, pady=2)







# Hover effects
for btn in [add_button, sub_button, multiply_button, divide_button]:
    btn.bind("<Enter>", on_enter)
    btn.bind("<Leave>", on_leave)




root.mainloop()
