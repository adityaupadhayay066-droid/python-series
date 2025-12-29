import tkinter

button_values = [
    ["AC", "+/-", "⌫", "÷"],
    ["7", "8", "9", "x"],
    ["4", "5", "6", "-"],
    ["1", "2", "3", "+"],
    ["%", "0", ".", "="]
]

right_symbol = ["+", "-", "=", "x", "÷"]
top_symbol = ["AC", "+/-", "⌫"]

bg = "#1E1E1E"
color_blue = "#2787F5"
color_white = "White"
color_black = "#1C1C1C"
color_orange = "#F59827"

ui = tkinter.Tk()
ui.title("Calculator")
ui.geometry("600x400")

buttons = ""
frame = tkinter.Frame(ui)
frame.grid(row=1, column=0)

label = tkinter.Label(
    ui,
    text="0",
    font=("Arial", 45),
    bg="#FFF7F5",
    fg="#1C1C1C",
    anchor="e"
)
label.grid(row=0, column=0, columnspan=4, sticky="we", pady=10, padx=10)

def button_clicked(value):
    global buttons
    if value == "AC":
        buttons = ""
    elif value == "⌫":
        buttons = buttons[:-1]
    elif value == "+/-":
        if buttons.startswith("-"):
            buttons = buttons[1:]
        else:
            buttons = "-" + buttons if buttons else ""
    elif value == "=":
        try:
            expr = buttons.replace("x", "*").replace("÷", "/").replace("%", "/100")
            result = str(eval(expr))
            buttons = result
        except:
            buttons = "Err"
    else:
        buttons += value

    label.config(text=buttons if buttons else "0")

for row in range(len(button_values)):
    for column in range(len(button_values[row])):
        value = button_values[row][column]
        button = tkinter.Button(
            frame,
            text=value,
            font=("Arial", 20),
            width=5,
            height=2,
            command=lambda value=value: button_clicked(value)
        )
        button.grid(row=row+1, column=column, padx=2, pady=2)

       
        if value in right_symbol:
            button.config(bg=color_orange, fg=color_white, borderwidth=0)
        elif value in top_symbol:
            button.config(bg="#2196F3", fg=color_white, borderwidth=0)
        else:
            button.config(bg="#424242", fg=color_white, borderwidth=0)

ui.update()
window_width = ui.winfo_width()
window_height = ui.winfo_height()
screen_width = ui.winfo_screenwidth()
screen_height = ui.winfo_screenheight()
x_cordinate = int((screen_width/2) - (window_width/2))
y_cordinate = int((screen_height/2) - (window_height/2))
ui.geometry(f"{window_width}x{window_height}+{x_cordinate}+{y_cordinate}")

ui.mainloop()

