import tkinter as tk
from tkinter import messagebox

# ---------------- QUESTIONS ----------------
questions = (
    "Q1): Who is the father of computer?",
    "Q2): What is the largest continent on Earth?",
    "Q3): Capital of Russia?",
    "Q4): Who is the first PM of India?",
    "Q5): Who is known as the missile man of India?",
    "Q6): Which planet is known as the Red Planet?",
    "Q7): What is the chemical symbol for gold?",
    "Q8): Which gas is most abundant in the Earth's atmosphere?",
    "Q9): Which is the longest river in the world?",
    "Q10): Which planet has the most moons?"
)

options = (
    ("A. Elon Musk", "B. Charles Babbage", "C. Alan Turing", "D. Steve Jobs"),
    ("A. Africa", "B. Asia", "C. America", "D. Antarctica"),
    ("A. Moscow", "B. Islamabad", "C. Thimpu", "D. Saint Petersburg"),
    ("A. Mahatma Gandhi", "B. Indira Gandhi", "C. Jawahar Lal Nehru", "D. Lal Bahadur Shastri"),
    ("A. Dr Abdul Kalam", "B. Narendra Modi", "C. Homi Bhabha", "D. Neil Armstrong"),
    ("A. Earth", "B. Mars", "C. Jupiter", "D. Venus"),
    ("A. Au", "B. Ag", "C. Gd", "D. Go"),
    ("A. Oxygen", "B. Nitrogen", "C. Carbon Dioxide", "D. Hydrogen"),
    ("A. Amazon", "B. Nile", "C. Ganga", "D. Yangtze"),
    ("A. Earth", "B. Jupiter", "C. Mars", "D. Venus")
)

answers = ("B", "B", "A", "C", "A", "B", "A", "B", "B", "B")

current_q = 0
score = 0
time_left = 10
timer_id = None

# ---------------- FUNCTIONS ----------------
def load_question():
    global time_left, timer_id

    if timer_id:
        ui.after_cancel(timer_id)

    question_label.config(text=questions[current_q])
    selected_option.set("")

    for i in range(4):
        radio_buttons[i].config(text=options[current_q][i])

    time_left = 10
    timer_label.config(text="Time Left: 10s", fg="green")
    update_timer()

def update_timer():
    global time_left, timer_id

    if time_left > 0:
        if time_left <= 2:
            timer_label.config(fg="red")
        elif time_left <= 5:
            timer_label.config(fg="orange")
        else:
            timer_label.config(fg="green")

        timer_label.config(text=f"Time Left: {time_left}s")
        time_left -= 1
        timer_id = ui.after(1000, update_timer)
    else:
        timer_label.config(text="Time Up!", fg="red")
        next_question(auto=True)

def next_question(auto=False):
    global current_q, score, timer_id

    if timer_id:
        ui.after_cancel(timer_id)

    if not auto and selected_option.get() == "":
        messagebox.showwarning("Warning ⚠️", "Please select an option")
        load_question()
        return

    if selected_option.get() == answers[current_q]:
        score += 1

    current_q += 1

    if current_q < len(questions):
        load_question()
    else:
        messagebox.showinfo(
            "Quiz Finished",
            f"Your Score: {score}/{len(questions)}"
        )
        ui.destroy()

# ---------------- GUI ----------------
ui = tk.Tk()
ui.title("Quiz App for Teenagers 👤")
ui.geometry("400x500")
ui.configure(bg="white")

timer_label = tk.Label(
    ui,
    text="Time Left: 10s",
    font=("Arial", 12, "bold"),
    bg="white",
    fg="green"
)
timer_label.pack(pady=5)

question_label = tk.Label(
    ui,
    font=("Arial", 14),
    wraplength=350,
    bg="white"
)
question_label.pack(pady=20)

selected_option = tk.StringVar()

radio_buttons = []
choices = ["A", "B", "C", "D"]

for i in range(4):
    rb = tk.Radiobutton(
        ui,
        font=("Arial", 12),
        anchor="w",
        variable=selected_option,
        value=choices[i],
        bg="white"
    )
    rb.pack(fill="x", padx=40)
    radio_buttons.append(rb)

next_btn = tk.Button(
    ui,
    text="Next ▶️",
    font=("Arial", 12),
    command=next_question,
    bg="lightblue",
    fg="black",
    activebackground="blue",
    activeforeground="white"
)
next_btn.pack(pady=20)

load_question()
ui.mainloop()


 
        





